from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

@frappe.whitelist()
def check_marks(doc, method):
    if doc.sslc < 1 or doc.hsc < 1:
        # if doc.hsc < 1 :
            frappe.errprint(doc.sslc)
            frappe.msgprint(_("mark should not be 0"))