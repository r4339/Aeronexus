document.addEventListener("DOMContentLoaded", () => {
    const loader = document.getElementById("loader");
    if (loader) {
        window.setTimeout(() => loader.remove(), 250);
    }

    const sidebar = document.querySelector(".sidebar");
    const toggle = document.getElementById("sidebarToggle");
    const overlay = document.getElementById("sidebarOverlay");

    const closeSidebar = () => {
        sidebar?.classList.remove("active");
        overlay?.classList.remove("show");
        toggle?.setAttribute("aria-expanded", "false");
    };

    toggle?.addEventListener("click", () => {
        const isOpen = sidebar?.classList.toggle("active");
        overlay?.classList.toggle("show", isOpen);
        toggle.setAttribute("aria-expanded", String(Boolean(isOpen)));
    });
    overlay?.addEventListener("click", closeSidebar);
    window.addEventListener("resize", () => {
        if (window.innerWidth >= 992) closeSidebar();
    });

    const clock = document.getElementById("liveClock");
    if (clock) {
        const renderClock = () => {
            clock.textContent = new Intl.DateTimeFormat("fr-FR", {
                weekday: "long", day: "numeric", month: "long", year: "numeric",
                hour: "2-digit", minute: "2-digit"
            }).format(new Date());
        };
        renderClock();
        window.setInterval(renderClock, 30_000);
    }

    document.querySelectorAll(".alert").forEach((alert) => {
        window.setTimeout(() => bootstrap.Alert.getOrCreateInstance(alert).close(), 4500);
    });

    const search = document.getElementById("searchInput");
    search?.addEventListener("input", () => {
        const term = search.value.toLocaleLowerCase("fr");
        document.querySelectorAll("tbody tr").forEach((row) => {
            row.hidden = !row.textContent.toLocaleLowerCase("fr").includes(term);
        });
    });
});
