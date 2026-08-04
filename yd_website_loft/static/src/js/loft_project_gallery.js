/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.LoftProjectGallery = publicWidget.Widget.extend({
    selector: ".o_loft_project_gallery",
    events: {
        mouseenter: "_onEnter",
        mouseleave: "_onLeave",
    },

    start() {
        this.images = this.el.querySelectorAll(".o_loft_gallery_img");
        this.dots = this.el.querySelectorAll(".o_loft_dot");
        this.index = 0;
        this.interval = null;
        return this._super(...arguments);
    },

    _onEnter() {
        if (this.images.length <= 1) return;
        this.interval = setInterval(() => {
            this.images[this.index].classList.remove("active");
            this.dots[this.index] && this.dots[this.index].classList.remove("active");
            this.index = (this.index + 1) % this.images.length;
            this.images[this.index].classList.add("active");
            this.dots[this.index] && this.dots[this.index].classList.add("active");
        }, 900);
    },

    _onLeave() {
        clearInterval(this.interval);
        this.images.forEach((img, i) => img.classList.toggle("active", i === 0));
        this.dots.forEach((dot, i) => dot.classList.toggle("active", i === 0));
        this.index = 0;
    },
});

export default publicWidget.registry.LoftProjectGallery;