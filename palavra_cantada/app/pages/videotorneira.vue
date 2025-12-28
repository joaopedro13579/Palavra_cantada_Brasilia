<template>
  <ClientOnly>
    <div class="video-container">
      <video
        ref="video"
        class="video"
        muted
        playsinline
        preload="auto"
        @ended="goHome"
        @pause="onPause"
        @stalled="goHome"
        @error="goHome"
        @waiting="onWaiting"
      >
        <source src="/video/placeholder.mp4" type="video/mp4" />
      </video>
    </div>
  </ClientOnly>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'

const video = ref(null)
let safetyTimer = null

const goHome = () => {
  clearTimeout(safetyTimer)
  navigateTo('/torneira')
}

const onPause = () => {
  // evita voltar se for pausa no final do vídeo
  if (video.value && !video.value.ended) {
    goHome()
  }
}

const onWaiting = () => {
  // se ficar travado mais de 3s, volta
  safetyTimer = setTimeout(goHome, 3000)
}

onMounted(async () => {
  await nextTick()
  const el = video.value
  if (!el) return

  el.addEventListener(
    'canplaythrough',
    async () => {
      try {
        el.muted = false
        el.volume = 1
        await el.play()
      } catch {}
    },
    { once: true }
  )
})
</script>

<style>
.video-container {
  width: 100vw;
  height: 100vh;
  background-color: #0b3c8a;
}

.video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
