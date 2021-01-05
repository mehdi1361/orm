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

        const liXb = document.createElement('li');
        liXb.className = 'xb';
        // liXb.innerText = `<svg xmlns='http://www.w3.org/2000/svg' width='512' height='512' viewBox='0 0 512 512'><path d='M126.8,248.3c39.7-58.6,77.9-92.8,77.9-92.8s-42.1-48.9-92.8-67.4l-3.3-.8A224.13,224.13,0,0,0,77.2,391C77.2,386.6,77.8,320.7,126.8,248.3Z'/><path d='M480,256A223.71,223.71,0,0,0,403.4,87.3l-3.2.9c-50.7,18.5-92.9,67.4-92.9,67.4s38.2,34.2,77.9,92.8c49,72.4,49.6,138.3,49.5,142.7A222.8,222.8,0,0,0,480,256Z'/><path d='M201.2,80.9c29.3,13.1,54.6,34.6,54.6,34.6s25.5-21.4,54.8-34.6c36.8-16.5,64.9-11.3,72.3-9.5a224.06,224.06,0,0,0-253.8,0C136.3,69.6,164.3,64.3,201.2,80.9Z'/><path d='M358.7,292.9C312.4,236,255.8,199,255.8,199s-56.3,37-102.7,93.9c-39.8,48.9-54.6,84.8-62.6,107.8l-1.3,4.8a224,224,0,0,0,333.6,0l-1.4-4.8C413.4,377.7,398.5,341.8,358.7,292.9Z'/></svg>`;
        el.append(liXb);

        const liWn = document.createElement('li');
        liWn.className = 'wn';
        // liWn.innerText = `<svg xmlns='http://www.w3.org/2000/svg' width='512' height='512' viewBox='0 0 512 512'><path d='M480,265H232V444l248,36V265Z'/><path d='M216,265H32V415l184,26.7V265Z'/><path d='M480,32,232,67.4V249H480V32Z'/><path d='M216,69.7,32,96V249H216V69.7Z'/></svg>`;
        el.append(liWn);

        return el;
    }
    getPrice() {
        const el = document.createElement('div');
        el.className = "card__price";

        const txt = document.createTextNode(`<span>5600 تومان</span><s>4300 تومان</s><b>30% تخفیف</b>`);
        el.append(txt);

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
        const svgNode = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        // svgNode.width = '512';
        // svgNode.height = '512';
        // svgNode.viewBox = '0 0 512 512';

        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        // path.setAttribute('d', 'M352.92,80C288,80,256,144,256,144s-32-64-96.92-64C106.32,80,64.54,124.14,64,176.81c-1.1,109.33,86.73,187.08,183,252.42a16,16,0,0,0,18,0c96.26-65.34,184.09-143.09,183-252.42C447.46,124.14,405.68,80,352.92,80Z');
        path.style.fill = "none";
        path.style.strokeLinecap = "round";
        path.style.strokeLinejoin = "round";
        path.style.strokeWidth = "32px";
        svgNode.append(path);
        b2.append(svgNode);

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
