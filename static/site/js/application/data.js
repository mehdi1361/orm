url = 'http://127.0.0.1:8000';

class Data {
      getData(url) {
         return fetch(url)
             .then(response => {return response.json()});
      }
      async getCategory() {
          return await this.getData(`${url}/api/v1/base/category/`);

      }

}