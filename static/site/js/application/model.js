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

class BigCard {

}

class Slider {
    constructor() {
        this.classList = ['section', 'section--bg', 'section--first'];
        this.background = "{% static 'site/img/bg.jpg' %}";
    }
    render() {
        const el = document.createElement('section');
        el.classList.add(...this.classList);
        el.setAttribute("data-bg", this.background);
        el.innerHTML += `<div class="container">
                <div class="row">
                    <!-- title -->
                    <div class="col-12">
                        <div class="section__title-wrap">
                            <h2 class="section__title section__title--title"><b>بهترین</b> بازی/فیلم های این ماه</h2>
    
                            <div class="section__nav-wrap">
                                <button class="section__nav section__nav--bg section__nav--prev" type="button" data-nav="#carousel0">
                                    <svg xmlns='http://www.w3.org/2000/svg' width='512' height='512' viewBox='0 0 512 512'><polyline points='184 112 328 256 184 400' style='fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:48px'/></svg>
                                </button>
                                <button class="section__nav section__nav--bg section__nav--next" type="button" data-nav="#carousel0">
                                    <svg xmlns='http://www.w3.org/2000/svg' width='512' height='512' viewBox='0 0 512 512'><polyline points='328 112 184 256 328 400' style='fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:48px'/></svg>
                                </button>
                            </div>
                        </div>
                    </div>
                    <!-- end title -->
                </div>
            </div>`;
        return el;
    }
}
