
const  superagent = require('superagent');

class Utils {
    async sleep(t) {
        return new Promise(resolve => {
            setTimeout(() => {
                resolve();
            }, t);
        });
    }
    async apiCall(method, params) {
        const res = await superagent.post('/api/jsonrpc')
            .send({
                method,
                params,
                "jsonrpc": "2.0",
                "id": 0
            }) // sends a JSON post body
            .set('X-API-Key', 'foobar')
            .set('accept', 'json')
        if(res.status == 200) {
            return res.body && res.body.result
        }else {
            new Error('网络请求失败', res)
        }
    }
}

module.exports = new Utils()
