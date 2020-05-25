// 循环读取服务端的状态
import { useEffect, useState } from 'react'
import utils from './utils'

export  function userLooper() {

    useEffect(()=>{
        loop()
    }, [])

    const [position, setPosition] = useState([]);
  
    const asyncStatus = async () => {
        const res = await utils.apiCall('get_position')
        if(res) {
            setPosition(res.position)
        }
    }

    const loop = async () => { 
        while(true) {
            await asyncStatus()
            await utils.sleep(1000)
        }
    }
  
    
    return {position}
  }
  

// class Looper {
//     position = [0, 0]
//     asyncStatus = async () => {
//         const res = await utils.apiCall('get_position')
//         if(res) {
//             this.position = res.position
//         }
//     }
// }
