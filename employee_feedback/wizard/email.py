from odoo import api, models, fields


class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    def _action_send_mail(self, auto_commit=False):
        if self.model == 'employee.feedback':
            self = self.with_context(mailing_document_based=True)
            if self.env.context.get('mark_so_as_sent'):
                self = self.with_context(mail_notify_author=self.env.user.partner_id in self.partner_ids)
        return super(MailComposeMessage, self)._action_send_mail(auto_commit=auto_commit)
