<!-- 根目录/error.vue -->
<template>
  <NuxtLayout name="default">
    <div class="app-error-chino">
      <img src="~/assets/img/chino.png" alt="智乃" />
      <h1>{{ error.statusCode }}</h1>
      <p>Are You Lost? There's Nothing Here At Chino's Blog.</p>
      <NuxtLink to="/">Let's Go Back To The Starting Point.</NuxtLink>
    </div>
  </NuxtLayout>
</template>

<script setup>
const props = defineProps({
  error: {
    type: Object,
    required: true
  }
})

const error = props.error
</script>

<style scoped>
.app-error-chino {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  width: 100%;
  height: calc(100vh - 128px);
}

.app-error-chino img {
  max-width: 100%;
  height: auto;
  width: 20%;
}

.app-error-chino h1 {
  font-size: 64px;
}

@media (max-aspect-ratio: 1/1) {
  .app-error-chino img {
    width: 50%;
  }

  .app-error-chino h1 {
    font-size: 48px;
  }
}
</style>