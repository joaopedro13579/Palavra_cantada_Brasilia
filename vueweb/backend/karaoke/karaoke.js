import { Gpio } from 'onoff'
import WebSocket, { WebSocketServer } from 'ws'

// WebSocket
const wss = new WebSocketServer({ port: 3001 })

const broadcast = (msg) => {
  const data = JSON.stringify(msg)
  wss.clients.forEach(c => {
    if (c.readyState === WebSocket.OPEN) {
      c.send(data)
    }
  })
}

// Botões → páginas/vídeos
const buttons = [
  { pin: 5, page: 'video1' },
  { pin: 6, page: 'video2' },
  { pin: 13, page: 'video3' },
  { pin: 19, page: 'video4' },
  { pin: 26, page: 'video5' }
]

buttons.forEach(({ pin, page }) => {
  const btn = new Gpio(pin, 'in', 'rising', {
    debounceTimeout: 150
  })

  btn.watch((err) => {
    if (err) return console.error(err)

    console.log(`🎵 Botão ${pin} → ${page}`)
    broadcast({
      type: 'button',
      page
    })
  })
})

// Cleanup
process.on('SIGINT', () => {
  buttons.forEach(({ pin }) => {
    const btn = new Gpio(pin, 'in')
    btn.unexport()
  })
  process.exit()
})

console.log('🟢 Karaoke buttons server rodando na porta 3001')
