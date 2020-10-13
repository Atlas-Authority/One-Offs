/*

Given an AGILE BOARD (not dashboard) ID and a group, this code will:

Find the filterID linked to the agile board
Check if the group is an admin of the board
If the 3rd parameter = 0, then if the group isn't an admin, it will be made an admin
Check if the group has edit permissions on the filter
If the 3rd parameter = 0, then if the group isn't an editor on the dashboard, it will be made an editor
Run the Botron cache clear and the UI will reflect this change

SELECT fixBoardAccess(1234,'jira-administrators',0);

Change the 3rd parameter from 0 to 1 to enforce (actually make the changes)

The output (clear the cache at /secure/ManageAdvancedSettings.jspa) assumes you have Botron config manager, if you don't - you could use ScriptRunner to clear the cache, or, if all else fails, restart the Jira application as the DB values are cached and just updating the DB does not mean the UI knows of the change

 */


CREATE OR REPLACE FUNCTION fixBoardAccess (
    boardID integer,
    targetGroupName text,
    enforceRun integer DEFAULT 0
)
RETURNS text
AS $$
DECLARE
    filterID integer;
    desiredBoardAdmins integer;
    desiredFilterAdmins integer;
    filterAdminRights integer;
    sharePermID integer;
    shareCounter integer;
BEGIN

    IF enforceRun = 1 THEN
        raise notice 'Enforce run ON';
    ELSE
        raise notice 'Enforce run OFF';
    END IF;

    raise notice 'Target Group: %', targetGroupName;

    SELECT
        rv."SAVED_FILTER_ID"
    INTO
        filterID
    FROM
        "AO_60DB71_RAPIDVIEW" AS rv
    WHERE
        rv."ID" = boardID;

    raise notice 'BoardID % has filterID %', boardID, filterID;

    SELECT
        count(*)
    INTO
        desiredBoardAdmins
    FROM
        "AO_60DB71_RAPIDVIEW" AS rv
            LEFT JOIN "AO_60DB71_BOARDADMINS" AS bAdmins ON bAdmins."RAPID_VIEW_ID" = rv."ID"
    WHERE
        lower(bAdmins."KEY") = lower(targetGroupName)
        AND rv."ID" = boardID
        AND bAdmins."TYPE" = 'GROUP';

    raise notice 'Is % an admin of the board?: %', targetGroupName, desiredBoardAdmins;

    IF desiredBoardAdmins = 0 THEN
        raise notice 'No, we need to make % an admin of board %', targetGroupName, boardID;
        IF enforceRun = 1 THEN
            INSERT INTO "AO_60DB71_BOARDADMINS" ("KEY","RAPID_VIEW_ID","TYPE") VALUES (targetGroupName,boardID,'GROUP');
        END IF;
    END IF;

    SELECT
        count(*)
    INTO
        desiredFilterAdmins
    FROM
        searchrequest AS f,
        sharepermissions AS sp
    WHERE
        0=0
        AND sp.entityid = f.id
        AND f.id = filterID
        AND sp.sharetype = 'group'
        AND lower(sp.param1) = lower(targetGroupName)
        AND sp.entitytype = 'SearchRequest';

    raise notice 'Is % an admin of the filter?: %', targetGroupName, desiredFilterAdmins;

    IF desiredFilterAdmins > 0 THEN
        raise notice 'We have a group, but do they have the right permissions?';
        SELECT
            rights, sp.id
        INTO
            filterAdminRights, sharePermID
        FROM
            searchrequest AS f,
            sharepermissions AS sp
        WHERE
            0=0
            AND sp.entityid = f.id
            AND f.id = filterID
            AND sp.sharetype = 'group'
            AND lower(sp.param1) = lower(targetGroupName)
            AND sp.entitytype = 'SearchRequest';
        IF filterAdminRights < 3 THEN
          raise notice 'Time to elevate the rights for % using SP %', targetGroupName, sharePermID;
          IF enforceRun = 1 THEN
            UPDATE sharepermissions SET rights = 3 WHERE id = sharePermID;
          END IF;
        END IF;
    ELSE
        raise notice 'Need to create a share';
        SELECT seq_id INTO shareCounter FROM sequence_value_item WHERE seq_name = 'SharePermissions';
        raise notice 'Current Sequence: %', shareCounter;
        IF enforceRun = 1 THEN
            UPDATE sequence_value_item SET seq_id = seq_id + 10 WHERE seq_name = 'SharePermissions';
            INSERT INTO
                sharepermissions (id,entityid,entitytype,sharetype,param1,rights)
                VALUES (shareCounter,filterID,'SearchRequest','group',targetGroupName,3);
        END IF;
    END IF;

    RETURN 'All done - clear the cache at /secure/ManageAdvancedSettings.jspa to apply - if you are making multiple changes, please run the SQL updates in a batch and clear the cache once at the end';
END;
$$ language plpgsql;