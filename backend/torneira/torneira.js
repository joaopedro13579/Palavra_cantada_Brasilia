const express = require("express");
const path = require("path");
const WebSocket = require("ws");
const ads1x15 = require("ads1x15");

const app = express();
const PORT = 3000;

// Servir Vue

app.use(express.static(path.join(__dirname, "dist")));

app.use((req, res) => {
  res.sendFile(path.join(__dirname, "dist", "index.html"));
});


const server = app.listen(PORT, () =>
  console.log("Rodando em http://localhost:3000")
);

// WebSocket
const wss = new WebSocket.Server({ server });

// ADS1115
const i2c = require("i2c-bus");


// abre o barramento I2C explicitamente
const i2cBus = i2c.openSync(1);

// cria o ADC passando o bus
const adc = new ads1x15(i2cBus, {
  i2cAddress: 0x48,
  chip: "ADS1115"
});
const channel = 0;
const gain = 4096; // ±4.096V
const sampleRate = 250;

let lastVoltage = null;
const THRESHOLD = 0.05; // 50 mV (ajuste se necessário)
const COOLDOWN_MS = 500;
let lastTrigger = 0;

setInterval(() => {
  adc.readADCSingleEnded(channel, gain, sampleRate, (err, voltage) => {
    if (err) return console.error(err);

    if (lastVoltage === null) {
      lastVoltage = voltage;
      return;
    }

    const delta = Math.abs(voltage - lastVoltage);
    const now = Date.now();

    if (delta > THRESHOLD && now - lastTrigger > COOLDOWN_MS) {
      lastTrigger = now;

      wss.clients.forEach(client => {
        if (client.readyState === WebSocket.OPEN) {
          client.send(JSON.stringify({
            type: "POT_MOVED",
            voltage
          }));
        }
      });
    }

    lastVoltage = voltage;
  });
}, 100); // 10 Hz
