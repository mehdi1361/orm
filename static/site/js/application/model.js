class Category {
    constructor(id, name) {
        this.id = id;
        this.name = name;
    }

    renderCategory() {
        const el = document.createElement('li');
        el.innerHTML = `<a href="#category_${this.name.toString().toLowerCase()}">${this.name}</a>`;
        return el;
    }
}