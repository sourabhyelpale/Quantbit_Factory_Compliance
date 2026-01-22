// Copyright (c) 2026, Quantbit Technologies and contributors
// For license information, please see license.txt


frappe.ui.form.on("Factory Regulatory Register", {
    setup(frm) {

        frm.set_query("compliance", () => {
            return {
                filters: {
                    disable: 0
                }
            };
        });

        frm.set_query("license", () => {
            return {
                filters: {
                    disable: 0
                }
            };
        });

    }
});

