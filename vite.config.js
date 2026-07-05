import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), tailwindcss()],
  envDir: '..',
  envPrefix: ['VITE_', 'RNG_SHOWCASE_'],
  server: {
    fs: {
      allow: ['..']
    }
  }
})
