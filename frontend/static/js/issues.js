(function () {
    const items = document.querySelectorAll(".issues-content .item");
    let lastSelected = null;

    addEventListenerForQuery(items, "click", function() {
        if (lastSelected != null) {
            lastSelected.classList.remove("active");
        }

        this.classList.add("active");
        lastSelected = this;
    });
})();
