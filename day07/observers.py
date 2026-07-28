class SMSAlert:
    """
    Observer 1:
    Sends account activity notifications.
    """

    def update(self, event):

        print(
            f"[SMS Alert] {event}"
        )


class AuditLog:
    """
    Observer 2:
    Records account activities.
    """

    def update(self, event):

        print(
            f"[Audit Log] {event}"
        )