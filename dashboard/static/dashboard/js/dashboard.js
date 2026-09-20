document.addEventListener('DOMContentLoaded', function () {
    var sidebar = document.getElementById('sidebar');

    var mobileToggle = document.getElementById('sidebar-toggle');
    if (mobileToggle && sidebar) {
        mobileToggle.addEventListener('click', function () {
            sidebar.classList.toggle('show');
        });
    }

    var desktopToggle = document.getElementById('desktop-sidebar-toggle');
    if (desktopToggle) {
        desktopToggle.addEventListener('click', function () {
            document.body.classList.toggle('sidebar-minimized');
        });
    }

    var fullscreenBtn = document.getElementById('btn-fullscreen');
    if (fullscreenBtn) {
        fullscreenBtn.addEventListener('click', function () {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(function () {});
            } else {
                document.exitFullscreen();
            }
        });
    }
});
