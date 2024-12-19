from django.dispatch import Signal, receiver
import logging
comment_update_logger = logging.getLogger('comment_update_logger')
commented_updated = Signal()

@receiver(commented_updated)
def log_comment_updation(sender, **kwargs):
    user = kwargs.get('user')
    comment_update_logger.info(f"Comment with the user '{user}' has been Updated.")
