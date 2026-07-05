<script setup>
import { ref } from 'vue'

const account = ref(null)
const guessNumber = ref(1)
const loading = ref(false)
const result = ref(null)

// Fungsi MOCK untuk menghubungkan Wallet (Simulasi UI)
const connectWallet = async () => {
  // Simulasi loading sebentar
  loading.value = true
  setTimeout(() => {
    account.value = "0x71C...976F" // Mock address
    loading.value = false
  }, 500)
}

// Fungsi MOCK utama Interaksi On-Chain (Simulasi UI)
const executeContract = async () => {
  if (guessNumber.value < 1 || guessNumber.value > 5) {
    alert("Input harus antara 1 sampai 5!")
    return
  }

  loading.value = true
  result.value = null

  // Simulasi proses transaksi (delay 2 detik)
  setTimeout(() => {
    const correctNum = Math.floor(Math.random() * 5) + 1
    
    result.value = {
      input: guessNumber.value,
      correctNumber: correctNum,
      won: guessNumber.value == correctNum
    }
    
    loading.value = false
  }, 2000)
}
</script>

<template>
  <div class="min-h-screen bg-white text-black flex items-center justify-center p-4 font-sans">
    <div class="p-8 w-full max-w-md text-center border-2 border-black">
      
      <h1 class="text-3xl font-black mb-8 text-black uppercase tracking-widest">
        Tebak Angka Web3
      </h1>

      <div v-if="!account">
        <p class="text-black mb-6 font-bold">Hubungkan wallet MetaMask Anda untuk mulai bermain.</p>
        <button 
          @click="connectWallet" 
          class="bg-black hover:bg-white hover:text-black text-white transition-colors px-6 py-3 font-bold w-full border-2 border-black uppercase tracking-wide"
        >
          Connect Wallet
        </button>
      </div>

      <div v-else>
        <div class="p-4 mb-6 flex justify-between items-center text-sm border-b-2 border-black">
          <span class="text-black font-bold uppercase">Wallet:</span>
          <span class="font-mono text-black font-bold">
            {{ account.slice(0, 6) }}...{{ account.slice(-4) }}
          </span>
        </div>

        <div class="mb-6 text-left">
          <label class="block text-black mb-2 font-bold uppercase tracking-wide">Tebak Angka (1-5):</label>
          <input 
            type="number" 
            v-model="guessNumber" 
            min="1" 
            max="5" 
            class="w-full p-4 bg-white text-black border-2 border-black focus:ring-4 focus:ring-black focus:outline-none transition-all font-mono text-xl"
          />
        </div>

        <button 
          @click="executeContract" 
          :disabled="loading" 
          class="bg-black text-white hover:bg-white hover:text-black transition-all px-6 py-4 font-bold w-full border-2 border-black disabled:opacity-50 disabled:cursor-not-allowed text-lg uppercase tracking-wider"
        >
          {{ loading ? 'Memproses...' : 'Tebak Sekarang!' }}
        </button>

        <div v-if="result" class="mt-8 p-6 border-2 border-black text-left">
          <h3 class="font-black text-xl mb-4 text-black uppercase border-b-2 border-black pb-2">Hasil Tebakan</h3>
          
          <div class="flex justify-between mb-2">
            <span class="text-black font-bold uppercase">Tebakan Anda:</span>
            <span class="font-mono font-bold text-black text-lg">{{ result.input }}</span>
          </div>
          
          <div class="flex justify-between mb-4">
            <span class="text-black font-bold uppercase">Angka Rahasia:</span>
            <span class="font-mono font-bold text-black text-lg">{{ result.correctNumber }}</span>
          </div>
          
          <div class="mt-4 pt-4 border-t-2 border-black text-center">
            <p 
              class="font-black text-xl uppercase tracking-widest mb-2" 
            >
              {{ result.won ? 'TEBAKAN BENAR!' : 'TEBAKAN SALAH!' }}
            </p>
            <p v-if="result.won" class="text-sm font-bold text-black text-left mt-4 border-l-4 border-black pl-4">
              Selamat! Tebakan Anda tepat. Token hadiah telah dikirim ke wallet Anda.
            </p>
            <p v-else class="text-sm font-bold text-black text-left mt-4 border-l-4 border-black pl-4">
              Sayang sekali, tebakan Anda belum tepat. Silakan coba lagi!
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* 
  Kosong karena semua styling murni menggunakan Tailwind CSS. 
  Pastikan Anda telah mengimpor tailwindcss di style.css utama!
*/
</style>
