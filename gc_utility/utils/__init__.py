# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _


__version__ = "0.0.1"


@frappe.whitelist()
def clear_email_queue():
    frappe.only_for("System Manager")
    frappe.enqueue(_truncate_email_queue)
    frappe.msgprint(
        _("Email Queue clearing has been enqueued. Please check after a few minutes")
    )


def _truncate_email_queue():
    frappe.db.sql("TRUNCATE TABLE `tabEmail Queue`")