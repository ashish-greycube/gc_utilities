frappe.listview_settings["Email Queue"] = {
  onload: function (me) {
    console.log("loaded");

    me.page.add_menu_item("Clear Email Queue", function () {
      frappe.call({
        method: "gc_utility.utils.clear_email_queue",
        freeze: true,
        args: {},
        callback: function (r) {},
      });
    });
  },
};
