# Need to delete like 20 unshared rapid boards?
# Put some ids in there like 1,2,3,4,5 and it'l delete em.
# Queries have to be run in this order.

delete from "A0_60DB71_BOARDADMINS" where "RAPID_VIEW_ID" in (<CSV Board IDs>)
delete from "A0_60DB71_CARDCOLOR" where "RAPID_VIEW_ID" in (<CSV Board IDs>)
delete from "A0_60DB71_COLUMNSTATUS" where "COLUMN_ID" in (select id from "A0_60DB71_COLUMN" where "RAPID_VIEW_ID" in (<CSV Board IDs>))
delete from "A0_60DB71_COLUMN" where "RAPID_VIEW_ID" in (<CSV Board IDs>)
delete from "A0_60DB71_DETAILVIEWFIELD" where "RAPID_VIEW_ID" in (<CSV Board IDs>)
delete from "A0_60DB71_ESTIMATESTATISTIC" where "RAPID_VIEW_ID" in (<CSV Board IDs>)
delete from "A0_60DB71_QUICKFILTER" where "RAPID_VIEW_ID" in (<CSV Board IDs>)
delete from "A0_60DB71_STATSFIELD" where "RAPID_VIEW_ID" in (<CSV Board IDs>)
delete from "A0_60DB71_SWIMLANE" where "RAPID_VIEW_ID" in (<CSV Board IDs>)
delete from "A0_60DB71_TRACKIN6STATISTIC" where "RAPID_VIEW_ID" in (<CSV Board IDs>)
delete from "A0_60DB71_NONWORKIN6DAV" where "WORKING_DAVS_ID" in (select id from "A0_60DB71_WORKINGDAYS" where "RAPID_VIEW_ID" in (<CSV Board IDs>))
delete from "A0_60DB71_WORKINGDAYS" where "RAPID_VIEW_ID" in (<CSV Board IDs>)
delete from "A0_60DB71_SUBQUERY" where "RAPID_VIEW_ID" in (<CSV Board IDs>)
delete from "A0_60DB71_RAPIDVIEW" where "ID" in (<CSV Board IDs>) 
