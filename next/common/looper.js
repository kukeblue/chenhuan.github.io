// 循环读取服务端的状态
import { useEffect, useState } from 'react'
import utils from './utils'

export  function userLooper({isloop = true}) {

    useEffect(()=>{
        loop()
    }, [])

    const [position, setPosition] = useState([]);
    const [mousePosition, setMousePosition] = useState([]);
    const [logData, setLogData] = useState('');
    
    const asyncStatus = async () => {
        const res = await utils.apiCall('get_position')
        if(res) {
            setPosition(res.position)
            setMousePosition(res.mouse_position)
            setLogData(res.log_data)
        }
    }

    const loop = async () => { 
        while(isloop) {
            await asyncStatus()
            await utils.sleep(1000)
        }
    }
  
    
    return {logData, position, mousePosition}
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
