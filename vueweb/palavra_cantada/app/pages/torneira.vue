<template>
  <!-- Imagem fullscreen (só visível quando carregada) -->
  <img
    v-show="imageLoaded"
    :src="'/torneira.png'"
    class="fullscreen-image"
    @load="onImageLoad"
    @error="onImageError"
  />

  <!-- Fallback com raios (só quando não tem imagem) -->
  <main v-if="!imageLoaded" class="home">
    <div class="rays"></div>

    <div class="content">
      <h1>Palavra Cantada</h1>
      <p>Ligue a torneira para começar</p>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const imageSrc = '/torneira.png'
const imageLoaded = ref(false)

onMounted(() => {
  const img = new Image()

  img.src = imageSrc

  img.onload = () => {
    imageLoaded.value = true
    console.log('✅ imagem carregada')
  }

  img.onerror = () => {
    imageLoaded.value = false
    console.log('❌ imagem não existe')
  }
})
</script>


<style scoped>
/* ===== Fallback ===== */
.home {
  position: absolute;
  inset: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: #0b3c8a;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  z-index: 2;
}

/* Conteúdo central */
.content {
  position: relative;
  z-index: 3;
  text-align: center;
  animation: fadeIn 1s ease-out;
}

h1 {
  font-size: 3rem;
  margin-bottom: 0.5rem;
}

p {
  font-size: 1.2rem;
  opacity: 0.9;
}

/* Raios */
.rays {
  position: absolute;
  inset: -50%;
  z-index: 1;
  background: repeating-conic-gradient(
    from 0deg,
    #1565c0 0deg 12deg,
    #1e88e5 12deg 24deg
  );
  animation: slowRotate 40s linear infinite;
}

/* ===== Imagem ===== */
.fullscreen-image {
  position: absolute;
  inset: 0;
  width: 100vw;
  height: 100vh;
  object-fit: cover;
  z-index: 1;
}

/* ===== Animações ===== */
@keyframes slowRotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
