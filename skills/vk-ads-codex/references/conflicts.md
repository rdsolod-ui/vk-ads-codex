# Проверенные расхождения, 2026-09-09

| Поверхности | Разница | Рабочее решение |
|---|---|---|
| Редактор результата / [PromoCode](https://ads.vk.ru/doc/api/object/LeadFormPromoCode) | UI: 30, API: 100 | Для конструктора ≤30; не заявлять, что API и UI имеют один предел |
| UI и справка / [Question](https://ads.vk.ru/doc/api/object/LeadFormQuestion) | общий required_answers против текста о постоянном is_required=true | Читать текущую форму и оба поля; не выдумывать управление каждым вопросом в UI |
| Справка уведомлений / [Notification](https://ads.vk.ru/doc/api/object/LeadFormNotification) | до 10 email в UI, до 16 destinations в API | Не разрешать 16 email по лимиту общего массива |
| [LeadForm](https://ads.vk.ru/doc/api/object/LeadForm) / UI | pages максимум 1, blocks максимум 5; в UI четыре шага настройки | Четыре шага конструктора не четыре API pages |
| [CRM quality](https://ads.vk.ru/help/general/lead_forms/lead_transfer) | общее обещание оптимизации и конкретное пояснение об оптимизации на лид | Не обещать оплату/квалификацию как цель без текущего подтверждения |
| [Subscriptions](https://ads.vk.ru/doc/api/resource/Subscriptions) / объект Subscription | примеры ошибок со старыми enum | Использовать текущий объект и подтверждать accepted choices перед записью |
| Эмодзи в результате / [форматы объявления](https://ads.vk.ru/help/features/formats) | UI может хранить эмодзи в результате; справка запрещает их в рекламном тексте | Разделять поверхности; не обещать универсальную модерацию |

При новом расхождении добавляйте источник, дату, наблюдение, область применения и решение. Слабый источник не должен молча переопределять сильный. Недостающие данные помечайте UNKNOWN.
