
import { Flex, WingBlank, WhiteSpace, Button, Switch } from 'antd-mobile'
import "./index.less"
import { useEffect, useState } from 'react'
import { userLooper } from '../common/looper'
import utils from '../common/utils'
import Input from 'antd-mobile/lib/input-item/Input'

export default function Home() {

  let { position, mousePosition, logData } = userLooper({isloop: true})

  return (
    <div className='page'>
      <Flex>
        <div className='game-container'>
          <div> 任务坐标: 227, 630 </div>
        </div>
        <div className='control-panel'>
          <WingBlank>
            <WhiteSpace/>
            <div> 窗口位置  {'' + position.toString()} </div>
            <div> 鼠标位置 {'' + mousePosition.toString()} </div>
            <WhiteSpace/>
            <WhiteSpace/>
            <WhiteSpace/>
            <div className='title'>
              当前执行: 任务
            </div>
            <div className='console'>
              {logData.split('#').map((text, index)=>{
                return <div key={'_' + index}> ● {text}</div>
              })}
            </div>
            <WhiteSpace/>
            <Flex>
              <Button onClick={()=>{
                utils.apiCall('find_text');
              }} type="primary" size="small" inline>任务1</Button>
            </Flex>
          </WingBlank>
        </div>
      </Flex>
      <div className='game-status-row'>
        {/* <div className='online'></div>  */}
        <div className='offline'></div>
        <div className='game-status-text'>链接失败</div>
      </div>
    </div>
  )
}
