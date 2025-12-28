<template>
  <!-- Imagem fullscreen -->
  <img
    v-show="imageLoaded"
    :src="imageSrc"
    class="fullscreen-image"
  />

  <!-- Fallback -->
  <main v-if="!imageLoaded" class="home">
    <div class="rays"></div>

    <div class="content">
      <h1 class="fonte">Palavra Cantada</h1>
      <p class="fonte">Escolha sua música</p>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'

/**
 * A imagem deve estar em:
 * /public/escolha.png
 */
const imageSrc = '/karaoke.png'
const imageLoaded = ref(false)

onMounted(() => {
  const img = new Image()
  img.src = imageSrc

  img.onload = () => {
    imageLoaded.value = true
    console.log('✅ imagem escolha carregada')
  }

  img.onerror = () => {
    imageLoaded.value = false
    console.log('❌ imagem escolha não existe')
  }
})
</script>

<style scoped>
/* ===== Fonte ===== */
.fonte {
  color: black;
}

/* ===== Fallback ===== */
.home {
  position: absolute;
  inset: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: #8a570bff;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Conteúdo central */
.content {
  position: relative;
  z-index: 2;
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
    #c00a0aff 0deg 12deg,
    #d9e43eff 12deg 24deg
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
