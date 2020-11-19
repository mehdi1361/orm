class initController {
     static init() {
        const categoryEl = document.getElementById('drpCategoryM');
        categoryEl.innerHTML = '';

        let fetchData =  new Data();
        fetchData.getCategory().then(result => {
            for (const item of result) {
                let category = new Category(item.id, item.name);
                categoryEl.append(category.renderCategory());
            }
        });

    }
}
