<?php


?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DEDSEC Instagram</title>
  <script>
    // Substitua pelo seu IP
    const meuIP = "123.45.67.89";

    // Função para verificar o IP do visitante
    async function verificarIP() {
      try {
        // Fazendo requisição para obter o IP
        const resposta = await fetch("https://api.ipify.org?format=json");
        const dados = await resposta.json();

        // Verifica se o IP é diferente do especificado
        if (dados.ip !== meuIP) {
          document.title = "Instagram";
        }
      } catch (erro) {
        console.error("Erro ao obter o IP:", erro);
      }
    }

    // Executa a verificação ao carregar a página
    window.onload = verificarIP;
  </script>
</head>
<body>
  <h1>Bem-vindo à DedSec Page</h1>
</body>
</html>
