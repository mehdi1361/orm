url = 'http://127.0.0.1:8000';

class Data {
      getData(url) {
         return fetch(url)
             .then(response => {return response.json()});
      }
      async getCategory() {
          return await this.getData(`${url}/api/v1/base/category/`);

      }

      getTop(counter) {
          var request = new XMLHttpRequest();
          request.open('GET', `${url}/api/v1/movie/top/${counter}`, false);
          request.send(null);
          if (request.status === 200) {
              console.log(typeof JSON.parse(request.responseText));
              console.log(JSON.parse(request.responseText));
              return JSON.parse(request.responseText);
          }

      }

}