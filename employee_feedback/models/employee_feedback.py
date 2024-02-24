from odoo import api, models, fields
import datetime


class EmployeeType(models.Model):
    _name = 'employee.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _description = 'Employee Type'

    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")
    last_week = fields.Date(string="last week")

    def action_button(self):
        current_date = datetime.date.today()
        self.last_week = current_date +datetime.timedelta(days=7)
        print("Current Date:", current_date)
        print("Last Week's Date:", self.last_week)


class EmployeeGFeedback(models.Model):
    _name = 'employee.feedback'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'type'
    _description = 'Employee Feedback'
    _order = 'created_by'

    type = fields.Many2one('employee.type', string="Type", required=True)
    created_by = fields.Char(default=lambda self: self.env.user.name, string="Created By", readonly=True)
    date = fields.Date(default=fields.Date.context_today, readonly=True)
    feedback_to = fields.Many2one('res.users', string="Feedback To")
    comment = fields.Text(string="Comment")
    state = fields.Selection([('draft', 'Draft'), ('sent', 'Sent')],
                             default="draft", readonly=True)

    def action_done(self):
        self.state = 'sent'

    def action_cancel(self):
        self.state = 'draft'
