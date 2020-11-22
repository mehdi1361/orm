class initController {
     static init() {
        let app = document.getElementById('app');
        app.innerHTML = '';
        const slider = new Slider();
        app.append(slider.render());
        // let fetchData =  new Data();
        // fetchData.getCategory().then(result => {
        //     for (const item of result) {
        //         let category = new Category(item.id, item.name);
        //         categoryEl.append(category.renderCategory());
        //     }
        // });

    }
}
