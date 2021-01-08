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
    constructor() {
    }
    getWrapper() {
        const el = document.createElement('div');
        el.className = "card__wrap";
        el.append(this.getCardTitle());
        el.append(this.getData());
        el.append(this.getPlatform());
        el.append(this.getPrice());
        el.append(this.getAction());

        return el;
    }

    getCardTitle() {
        const el = document.createElement('div');
        el.className = "card__title";

        const h3 = document.createElement('h3');

        const a = document.createElement('a');
        a.href = "details.html";
        a.text = "فیلم سینمایی tenet 2020";

        h3.append(a);
        el.append(h3);

        return el;

    }
    getData() {
        const ul = document.createElement('ul');
        ul.className = "card__list";

        const li1 = document.createElement('li');
        const span = document.createElement('span');
        const txt = document.createTextNode("انتشار :");
        span.append(txt)

        const dateStr = document.createTextNode("30.11.2018");
        li1.append(span);
        li1.append(dateStr);

        ul.append(li1);

        const li2 = document.createElement('li');
        const spanGenre = document.createElement("span");
        const txtGenreSpan = document.createTextNode("ژانر ها :");
        const txtGenre = document.createTextNode("علمی و تخیلی ، اکشن ، دلهره آور");

        spanGenre.append(txtGenreSpan);

        li2.append(spanGenre);
        li2.append(txtGenre);
        ul.append(li2);

        return ul;

    }
    getImg() {
        const a1 = document.createElement('a');
        a1.className = "card__cover";
        const img = document.createElement('img');
        img.src = '../static/site/img/cards/4.jpg';
        a1.append(img)
        return a1;
    }
    getPlatform() {
        const el = document.createElement('ul');
        el.className = "card__platforms";
        el.append(iconPlatform('ps'));
        el.append(iconPlatform('xb'));
        el.append(iconPlatform('wn'));
        el.append(iconPlatform('ap'));

        return el;
    }
    getPrice() {
        const el = document.createElement('div');
        el.className = "card__price";

        const span = document.createElement('span');
        const s = document.createElement('s');
        const b = document.createElement('b');

        // const txt = document.createTextNode(`<span>5600 تومان</span><s>4300 تومان</s><b>30% تخفیف</b>`);
        const spanTxt = document.createTextNode("5600 تومان");
        span.append(spanTxt);

        const sTxt = document.createTextNode('4300 تومان');
        s.append(sTxt);

        const bTxt = document.createTextNode("30% تخفیف");
        b.append(bTxt);

        el.append(span);
        el.append(s);
        el.append(b);
        return el;
    }
    getAction() {
        const el = document.createElement('div');
        el.className = "card__actions";

        const b1 = document.createElement('button');
        b1.className = "card__buy";
        b1.textContent = "خرید";
        el.append(b1);

        const b2 = document.createElement('button');
        b2.className = "card__favorite";

        const svgNode = new SvgObject("512", "512", "0 0 512 512", [
            new PathObject(
                'M352.92,80C288,80,256,144,256,144s-32-64-96.92-64C106.32,80,64.54,124.14,64,176.81c-1.1,109.33,86.73,187.08,183,252.42a16,16,0,0,0,18,0c96.26-65.34,184.09-143.09,183-252.42C447.46,124.14,405.68,80,352.92,80Z',
                {
                    "fill": "none",
                    "stroke-linecap": "round",
                    "stroke-linejoin": "round",
                    "stroke-width": "32px"
                })
        ])

        b2.append(svgNode.render());

        el.append(b2);

        return el;

    }

    render() {
        const el = document.createElement('div');
        el.classList.add(...["card", "card--big"]);
        el.append(this.getImg());
        el.append(this.getWrapper());
        return el;
    }
}
class BigCardScene {
    constructor() {
        this.classes = ["owl-carousel", "section__carousel", "section__carousel--big"];
    }

    render() {
        const el = document.createElement('div');
        el.id = "carousel0";
        el.classList.add(...this.classes);
        const card = new BigCard();
        el.append(card.render());
        return el;
    }

}

class SliderButton {
    constructor(classes, svg) {
        this.classList = [...classes];
        this.svg = svg;
    }
    render() {
        const el = document.createElement('button');
        el.classList.add(...this.classList);
        el.innerHTML = this.svg;
        return el;
    }
}

class Slider {
    constructor() {
        this.classList = ['section', 'section--bg', 'section--first'];
        this.background = "../static/site/img/bg.jpg";
    }
    render() {
        const btn1 = new SliderButton(
            ["section__nav", "section__nav--bg", "section__nav--prev"],
            `<svg xmlns='http://www.w3.org/2000/svg' width='512' height='512' 
                    viewBox='0 0 512 512'><polyline points='184 112 328 256 184 400' 
                    style='fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:48px'/></svg>`
        );
        const btn2 = new SliderButton(
            ["section__nav", "section__nav--bg", "section__nav--next"],
            `<svg xmlns='http://www.w3.org/2000/svg' width='512' height='512' viewBox='0 0 512 512'>
                  <polyline points='328 112 184 256 328 400' style='fill:none;
                  stroke-linecap:round;stroke-linejoin:round;stroke-width:48px'/></svg>`
        );

        const el = document.createElement('section');
        el.classList.add(...this.classList);
        el.setAttribute("data-bg", this.background);

        const container = document.createElement('div');
        container.className = "container";

        const row = document.createElement('div');
        row.className = "row";

        const col = document.createElement('div');
        col.className = "col-12";

        const sectionTitleWrap = document.createElement('div');
        sectionTitleWrap.className = "section__title-wrap";

        const h2 = document.createElement('h2');
        h2.classList.add(...["section__title", "section__title--title"]);
        const text = document.createTextNode("فیلم های منتخب");
        h2.appendChild(text);

        const sectionNavWrap = document.createElement('div');
        sectionNavWrap.className = "section__nav-wrap";
        sectionNavWrap.append(btn1.render(), btn2.render());

        sectionTitleWrap.append(h2, sectionNavWrap);
        col.append(sectionTitleWrap);
        row.append(col);
        container.append(row);
        el.append(container);
        const sliderScene = new BigCardScene();
        el.append(sliderScene.render());

        return el;
    }
}
