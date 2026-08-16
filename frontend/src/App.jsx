import { useState } from 'react'
import './App.css'

function App() {
  const [passport, setPassport] = useState(false)
  const [userMess, setUserMess] = useState('')
  const [aiAnswer, setAIAnswer] = useState('')

  const MessageAI = async (e)=>{
    e.preventDefault()

    const  response = await fetch("/api/message",
      {
        "method": 'POST',
        "headers": {
          'Content-Type': 'application/json'
        },
        'body': JSON.stringify({text: userMess, status: passport})
    }
    )
    const data = await response.json()
    setAIAnswer(data.content)

  }

  return (
    <>
      <section id="center">
        <label htmlFor="status">Статус: </label>
        <p className="status" id='status'>{passport ? 'Принят' : 'Не принят'}</p>
        <button type='button' className="change_status" onClick={()=> setPassport(prev => !prev)}>{passport ? 'Убрать паспорт' : 'Добавить паспорт'}</button>

        <form onSubmit={MessageAI} method="post">
          <input type="text" className="user_message" 
          value={userMess} onChange={(e) => setUserMess(e.target.value)}/>
          <button type="submit">Получить ответ ИИ</button>
          <p className="answer">{aiAnswer}</p>
        </form>
      </section>
    </>
  )
}

export default App
