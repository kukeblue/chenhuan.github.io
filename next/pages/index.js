
import { Flex, WingBlank, WhiteSpace, Button, Switch } from 'antd-mobile'
import "./index.less"
import { useEffect, useState } from 'react'
import { userLooper } from '../common/looper'

export default function Home() {

  let { position } = userLooper(0)

  return (
    <div className='page'>
      <Flex>
        <div className='game-container'>
        </div>
        <div className='control-panel'>
          <WingBlank>
            <WhiteSpace/>
            <div> 窗口位置 {position.toString()} </div>
            <WhiteSpace/>
            <WhiteSpace/>
            <WhiteSpace/>
            <div className='title'>
              当前执行: 任务
            </div>
            <div className='console'>
               
            </div>
            <WhiteSpace/>
            <Flex>
              {/* <Button type="primary" size="small" inline>停止</Button> */}
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
