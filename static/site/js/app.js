

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
        console.log("hash is", window.location.hash);
    }
}


window.addEventListener("hashchange", App.route);
App.init();