# Указатель HTTP-ресурсов

Извлечено из официальных страниц 2026-09-09. Пути и методы — навигация; обязательные поля и семантику операций читать по ссылке перед запросом. Отсутствие пути/метода в таблице не означает отсутствия функции.

| Ресурс | Методы на странице | Основные пути |
|---|---|---|
| [AdGroup](https://ads.vk.ru/doc/api/resource/AdGroup) | GET, POST, DELETE | `/api/v2/ad_groups/<ad_group_id>.json`<br>`/api/v2/ad_groups.json?fields=id,package_id`<br>`/api/v2/currencies.json` |
| [AdGroupMassAction](https://ads.vk.ru/doc/api/resource/AdGroupMassAction) | POST | `/api/v2/ad_groups/mass_action.json` |
| [AdGroups](https://ads.vk.ru/doc/api/resource/AdGroups) | GET, POST | `/api/v2/ad_groups.json`<br>`/api/v2/ad_groups.json?limit=10`<br>`/api/v2/ad_groups.json?limit=5&offset=15` |
| [AdPlan](https://ads.vk.ru/doc/api/resource/AdPlan) | GET, POST | `/api/v2/ad_plans/(?P<ad_plan_id>d+).json`<br>`/api/v2/ad_plans.json?fields=id,package_id` |
| [AdPlanMassAction](https://ads.vk.ru/doc/api/resource/AdPlanMassAction) | POST | `/api/v2/ad_plans/mass_action.json` |
| [AdPlans](https://ads.vk.ru/doc/api/resource/AdPlans) | GET, POST | `/api/v2/ad_plans.json`<br>`/api/v2/ad_plans.json?limit=10`<br>`/api/v2/ad_plans.json?limit=5&offset=15` |
| [AgencyClient](https://ads.vk.ru/doc/api/resource/AgencyClient) | POST, DELETE | `/api/v2/agency/clients/<id>.json` |
| [AgencyClients](https://ads.vk.ru/doc/api/resource/AgencyClients) | GET, POST | `/api/v2/agency/clients.json` |
| [AgencyManagerClient](https://ads.vk.ru/doc/api/resource/AgencyManagerClient) | POST, DELETE | `/api/v2/agency/managers/<manager_id>/clients/<client_id>.json`<br>`/api/v2/agency/managers/<manager_username>/clients/<client_username>.json` |
| [AppleApp](https://ads.vk.ru/doc/api/resource/AppleApp) | GET, POST | `/api/v2/apple_apps/<app_name>.json` |
| [AuditPixelCheck](https://ads.vk.ru/doc/api/resource/AuditPixelCheck) | POST | `/api/v3/audit_pixel.json` |
| [Banner](https://ads.vk.ru/doc/api/resource/Banner) | GET, POST, DELETE | `/api/v2/banners/<banner_id>.json` |
| [BannerFields](https://ads.vk.ru/doc/api/resource/BannerFields) | GET | `/api/v2/banner_fields.json` |
| [BannerMassAction](https://ads.vk.ru/doc/api/resource/BannerMassAction) | POST | `/api/v2/banners/mass_action.json` |
| [BannerPatterns](https://ads.vk.ru/doc/api/resource/BannerPatterns) | GET | `/api/v2/banner_patterns.json` |
| [BannerRemoderation](https://ads.vk.ru/doc/api/resource/BannerRemoderation) | POST | `/api/v2/banners/remoderate.json` |
| [Banners](https://ads.vk.ru/doc/api/resource/Banners) | GET | `/api/v2/banners.json`<br>`/api/v2/banners.json?_id=26617841`<br>`/api/v2/banners.json?_id__in=26617841,26711647` |
| [Content](https://ads.vk.ru/doc/api/resource/Content) | POST | `/api/v2/content/(static|video|html5).json` |
| [CounterGoal](https://ads.vk.ru/doc/api/resource/CounterGoal) | POST | `/api/v2/remarketing/counters/<counter_id>/goals/<goal_id>.json` |
| [CounterGoals](https://ads.vk.ru/doc/api/resource/CounterGoals) | GET, POST | `/api/v2/remarketing/counters/<counter_id>/goals.json` |
| [CreateUrl](https://ads.vk.ru/doc/api/resource/CreateUrl) | POST | `/api/v2/urls.json` |
| [Goals](https://ads.vk.ru/doc/api/resource/Goals) | GET | `/api/v2/goals.json` |
| [GoogleApp](https://ads.vk.ru/doc/api/resource/GoogleApp) | GET, POST | `/api/v2/google_apps/<app_name>.json` |
| [InAppEvent](https://ads.vk.ru/doc/api/resource/InAppEvent) | POST | `/api/v2/remarketing/inapp_events/<rb_mobile_app_id>/trackers/<tracker_id>/events/<inapp_event_id>.json` |
| [InAppEventCategories](https://ads.vk.ru/doc/api/resource/InAppEventCategories) | GET | `/api/v1/inapp_event_categories.json` |
| [LeadForm](https://ads.vk.ru/doc/api/resource/LeadForm) | GET, POST | `/api/v1/lead_ads/lead_forms/<lead_form_id>.json`<br>`/api/v1/lead_ads/lead_forms/17.json?get_active_form_ad_plans=1` |
| [LeadFormArchivation](https://ads.vk.ru/doc/api/resource/LeadFormArchivation) | POST | `/api/v1/lead_ads/lead_forms/archive` |
| [LeadFormCopy](https://ads.vk.ru/doc/api/resource/LeadFormCopy) | POST | `/api/v1/lead_ads/lead_forms/<lead_form_id>/copy` |
| [LeadFormImage](https://ads.vk.ru/doc/api/resource/LeadFormImage) | POST | `/api/v1/lead_ads/upload_image/<image_role>` |
| [LeadFormLeadsExport](https://ads.vk.ru/doc/api/resource/LeadFormLeadsExport) | GET | `/api/v1/lead_ads/lead_forms/<lead_form_id>/leads.<export_format>`<br>`/api/v1/lead_ads/lead_forms/17/leads.csv?_created_at__lte=2022-01-01%2000:00:00`<br>`/api/v1/lead_ads/lead_forms/17/leads.csv?_created_at__gte=2022-01-01%2000:00:00` |
| [LeadFormUnarchivation](https://ads.vk.ru/doc/api/resource/LeadFormUnarchivation) | POST | `/api/v1/lead_ads/lead_forms/unarchive` |
| [LeadForms](https://ads.vk.ru/doc/api/resource/LeadForms) | GET, POST | `/api/v1/lead_ads/lead_forms.json`<br>`/api/v1/lead_ads/lead_forms.json?limit=10`<br>`/api/v1/lead_ads/lead_forms.json?limit=5&offset=15` |
| [Leads](https://ads.vk.ru/doc/api/resource/Leads) | GET | `/api/v1/lead_ads/leads.json`<br>`/api/v1/lead_ads/leads.json?limit=10`<br>`/api/v1/lead_ads/leads.json?limit=5&offset=15` |
| [LocalGeo](https://ads.vk.ru/doc/api/resource/LocalGeo) | POST, DELETE | `/api/v2/remarketing/local_geo/1234.json` |
| [LocalGeos](https://ads.vk.ru/doc/api/resource/LocalGeos) | GET, POST | `/api/v2/remarketing/local_geo.json` |
| [ManagerClients](https://ads.vk.ru/doc/api/resource/ManagerClients) | GET | `/api/v3/manager/clients.json` |
| [MobileApps](https://ads.vk.ru/doc/api/resource/MobileApps) | GET | `/api/v1/mobile_app_users.json` |
| [MobileCategory](https://ads.vk.ru/doc/api/resource/MobileCategory) | GET | `/api/v2/mobile_categories.json` |
| [MobileOperationSystem](https://ads.vk.ru/doc/api/resource/MobileOperationSystem) | GET | `/api/v2/mobile_os.json` |
| [MobileOperator](https://ads.vk.ru/doc/api/resource/MobileOperator) | GET | `/api/v2/mobile_operators.json` |
| [MobileTypes](https://ads.vk.ru/doc/api/resource/MobileTypes) | GET | `/api/v2/mobile_types.json` |
| [MobileVendors](https://ads.vk.ru/doc/api/resource/MobileVendors) | GET | `/api/v2/mobile_vendors.json` |
| [OfferBatchTaskCreate](https://ads.vk.ru/doc/api/resource/OfferBatchTaskCreate) | GET, POST, PUT, DELETE | `/api/v2/remarketing/pricelists/<pricelist_id>/batch.json` |
| [OfferBatchTaskDetail](https://ads.vk.ru/doc/api/resource/OfferBatchTaskDetail) |  | `/api/v2/remarketing/pricelists/<pricelist_id>/batch/<task_id>.json` |
| [OrdAgencyAct](https://ads.vk.ru/doc/api/resource/OrdAgencyAct) | GET, POST | `/api/v2/ord/agency/<client_id>/acts.json`<br>`/api/v2/ord/agency/2147483647/acts.json?_month=2024-10-01` |
| [OrdAgencyActs](https://ads.vk.ru/doc/api/resource/OrdAgencyActs) | GET | `/api/v2/ord/agency/acts.json`<br>`/api/v2/ord/agency/acts.json?limit=50&offset=100$=&_month=2024-10-01&_client_id__in=123,445` |
| [OrdAgencyReport](https://ads.vk.ru/doc/api/resource/OrdAgencyReport) | GET | `/api/v2/ord/agency/report.json`<br>`/api/v2/ord/agency/report.json?limit=50&offset=100$=&_month=2024-10-01&_q=2147483647&sorting=` |
| [OrdAgencyStatus](https://ads.vk.ru/doc/api/resource/OrdAgencyStatus) | GET, POST | `/api/v2/ord/agency/status.json` |
| [OrdPartnerActStat](https://ads.vk.ru/doc/api/resource/OrdPartnerActStat) | GET | `/api/v1/ord/partner/acts/<month>.json` |
| [OrdPartnerActStatByPadId](https://ads.vk.ru/doc/api/resource/OrdPartnerActStatByPadId) | GET, POST | `/api/v1/ord/partner/acts/<month>/<ord_pad_id>.json` |
| [OrdPartnerPad](https://ads.vk.ru/doc/api/resource/OrdPartnerPad) | POST | `/api/v1/ord/partner/pads/<ord_pad_id>.json` |
| [OrdPartnerPads](https://ads.vk.ru/doc/api/resource/OrdPartnerPads) | GET | `/api/v1/ord/partner/pads.json` |
| [OrdPartnerSubAgent](https://ads.vk.ru/doc/api/resource/OrdPartnerSubAgent) | GET, POST | `/api/v1/ord/partner/subagents/<id>.json` |
| [OrdPartnerSubAgents](https://ads.vk.ru/doc/api/resource/OrdPartnerSubAgents) | GET, POST | `/api/v1/ord/partner/subagents.json` |
| [OrdUser](https://ads.vk.ru/doc/api/resource/OrdUser) | GET, POST | `/api/v2/ord_user.json` |
| [Packages](https://ads.vk.ru/doc/api/resource/Packages) | GET | `/api/v2/packages.json` |
| [PackagesPads](https://ads.vk.ru/doc/api/resource/PackagesPads) | GET | `/api/v2/packages_pads.json` |
| [PadsTree](https://ads.vk.ru/doc/api/resource/PadsTree) | GET | `/api/v2/pads_trees.json` |
| [ProjectionPrediction](https://ads.vk.ru/doc/api/resource/ProjectionPrediction) | POST | `/api/v3/projection.json` |
| [ReadUrl](https://ads.vk.ru/doc/api/resource/ReadUrl) | GET | `/api/v2/urls/<url_id>.json` |
| [ReadUrls](https://ads.vk.ru/doc/api/resource/ReadUrls) | GET | `/api/v2/urls/<url_id1>,<url_id2>,<url_id3>.json` |
| [Region](https://ads.vk.ru/doc/api/resource/Region) | GET | `/api/v2/regions.json`<br>`/api/v2/regions.json?_id=53`<br>`/api/v2/regions.json?_id__in=53,188` |
| [RemarketingCounter](https://ads.vk.ru/doc/api/resource/RemarketingCounter) | GET, POST, DELETE | `/api/v2/remarketing/counters/<counter_id>.json` |
| [RemarketingCounters](https://ads.vk.ru/doc/api/resource/RemarketingCounters) | GET, POST | `/api/v2/remarketing/counters.json`<br>`/api/v2/remarketing/counters.json?_counter_id=250000`<br>`/api/v2/remarketing/counters.json?_counter_id__in=250000,250001` |
| [RemarketingInAppEvents](https://ads.vk.ru/doc/api/resource/RemarketingInAppEvents) | GET | `/api/v2/remarketing/inapp_events.json`<br>`/api/v2/remarketing/inapp_events.json?_url_object_id=com.test` |
| [RemarketingOfflineGoal](https://ads.vk.ru/doc/api/resource/RemarketingOfflineGoal) | POST, DELETE | `/api/v2/remarketing/offline_goals/<id>.json` |
| [RemarketingOfflineGoals](https://ads.vk.ru/doc/api/resource/RemarketingOfflineGoals) | GET, POST | `/api/v2/remarketing/offline_goals.json` |
| [RemarketingUsersList](https://ads.vk.ru/doc/api/resource/RemarketingUsersList) | GET, POST, DELETE | `/api/v3/remarketing/users_lists/<id>.json` |
| [RemarketingUsersLists](https://ads.vk.ru/doc/api/resource/RemarketingUsersLists) | GET, POST | `/api/v3/remarketing/users_lists.json` |
| [Respondents](https://ads.vk.ru/doc/api/resource/Respondents) | GET | `/api/v1/lead_ads/respondents.json`<br>`/api/v1/lead_ads/respondents.json?limit=10`<br>`/api/v1/lead_ads/respondents.json?limit=5&offset=15` |
| [Segment](https://ads.vk.ru/doc/api/resource/Segment) | GET, POST, DELETE | `/api/v2/remarketing/segments/<id>.json` |
| [SegmentRelation](https://ads.vk.ru/doc/api/resource/SegmentRelation) | POST, DELETE | `/api/v2/remarketing/segments/<segment_id>/relations/<id>.json` |
| [SegmentRelations](https://ads.vk.ru/doc/api/resource/SegmentRelations) | GET, POST | `/api/v2/remarketing/segments/<segment_id>/relations.json` |
| [SegmentRelationsDelete](https://ads.vk.ru/doc/api/resource/SegmentRelationsDelete) | DELETE | `/api/v2/remarketing/segments/<segment_id>/relations/<id>,<id>+.json` |
| [Segments](https://ads.vk.ru/doc/api/resource/Segments) | GET, POST | `/api/v2/remarketing/segments.json` |
| [SharingKey](https://ads.vk.ru/doc/api/resource/SharingKey) | GET, POST | `/api/v2/sharing_keys.json` |
| [SharingKeyUser](https://ads.vk.ru/doc/api/resource/SharingKeyUser) | POST, DELETE | `/api/v2/sharing_keys/<key>.json` |
| [SkAdNetworkIdentityShare](https://ads.vk.ru/doc/api/resource/SkAdNetworkIdentityShare) | POST | `/api/v2/apple_apps/<app_id>/sk_ad_network_ids/share.json` |
| [SkAdNetworkIdentityWithdraw](https://ads.vk.ru/doc/api/resource/SkAdNetworkIdentityWithdraw) | POST | `/api/v2/apple_apps/<app_id>/sk_ad_network_ids/withdraw.json` |
| [Subscription](https://ads.vk.ru/doc/api/resource/Subscription) | DELETE | `/api/v3/subscription/<subscription_id>.json` |
| [Subscriptions](https://ads.vk.ru/doc/api/resource/Subscriptions) | GET, POST | `/api/v3/subscription.json` |
| [Survey](https://ads.vk.ru/doc/api/resource/Survey) | GET, POST | `/api/v1/lead_ads/survey_forms/<survey_id>.json`<br>`/api/v1/lead_ads/survey_forms/17.json?get_active_form_ad_plans=1` |
| [SurveyArchivation](https://ads.vk.ru/doc/api/resource/SurveyArchivation) | POST | `/api/v1/lead_ads/survey_forms/archive` |
| [SurveyCopy](https://ads.vk.ru/doc/api/resource/SurveyCopy) | POST | `/api/v1/lead_ads/survey_forms/<survey_id>/copy` |
| [SurveyRespondentsExport](https://ads.vk.ru/doc/api/resource/SurveyRespondentsExport) | GET | `/api/v1/lead_ads/survey_forms/<survey_id>/respondents.xlsx`<br>`/api/v1/lead_ads/survey_forms/17/respondents.xlsx?_created_at__lte=2022-01-01%2000:00:00`<br>`/api/v1/lead_ads/survey_forms/17/respondents.xlsx?_created_at__gte=2022-01-01%2000:00:00` |
| [SurveyUnarchivation](https://ads.vk.ru/doc/api/resource/SurveyUnarchivation) | POST | `/api/v1/lead_ads/survey_forms/unarchive` |
| [Surveys](https://ads.vk.ru/doc/api/resource/Surveys) | GET, POST | `/api/v1/lead_ads/survey_forms.json`<br>`/api/v1/lead_ads/survey_forms.json?limit=10`<br>`/api/v1/lead_ads/survey_forms.json?limit=5&offset=15` |
| [TargetingsTree](https://ads.vk.ru/doc/api/resource/TargetingsTree) | GET | `/api/v2/targetings_tree.json` |
| [TestLeadSending](https://ads.vk.ru/doc/api/resource/TestLeadSending) | POST | `/api/v1/lead_ads/lead_forms/<lead_form_id>/send_test_lead` |
| [Transaction](https://ads.vk.ru/doc/api/resource/Transaction) | POST | `/api/v2/billing/transactions/<mode>/<user_id>.json` |
| [TransactionGroups](https://ads.vk.ru/doc/api/resource/TransactionGroups) | GET | `/api/v2/billing/transaction_groups.json` |
| [User](https://ads.vk.ru/doc/api/resource/User) | GET, POST | `/api/v3/user.json` |
| [UserGeo](https://ads.vk.ru/doc/api/resource/UserGeo) | GET | `/api/v2/user_geo.json`<br>`/api/v2/user_geo.json?limit=10`<br>`/api/v2/user_geo.json?limit=5&offset=15` |
