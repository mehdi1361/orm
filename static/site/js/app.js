

const App = {
    init:  function() {
        initController.init();
    },
    route: function() {
        switch (window.location.hash) {
            case "#home":
                initController.init();
                break;
            default:
                console.log("exit...");
        }
    }
}


window.addEventListener("hashchange", App.route);
App.init();