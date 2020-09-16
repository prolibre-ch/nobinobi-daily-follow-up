# -*- coding: utf-8
from django.apps import AppConfig
from django.db.models.signals import post_delete, pre_save, post_migrate, post_save


class NobinobiDailyFollowUpConfig(AppConfig):
    name = 'nobinobi_daily_follow_up'

    def ready(self):
        import nobinobi_daily_follow_up.signals as signals
        from nobinobi_daily_follow_up.models import Meal, Medication, DailyFollowUp, GiveMedication
        post_delete.connect(signals.auto_delete_image_on_delete, sender=Meal)
        pre_save.connect(signals.auto_delete_image_on_change, sender=Meal)
        post_delete.connect(signals.auto_delete_attachment_on_delete, sender=Medication)
        pre_save.connect(signals.auto_delete_attachment_on_change, sender=Medication)
        post_migrate.connect(signals.create_group_nobinobi_daily_follow_up, sender=self)
        post_migrate.connect(signals.create_group_admin_nobinobi_daily_follow_up, sender=self)
        post_save.connect(signals.medication_on_daily_follow_up, sender=DailyFollowUp)
        post_delete.connect(signals.delete_notification_after_delete_givemedication, sender=GiveMedication)
        post_save.connect(signals.create_notification_after_save_givemedication, sender=GiveMedication)
        post_save.connect(signals.create_troubleshooting_in_daily_follow_up, sender=DailyFollowUp)
