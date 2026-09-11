/*
  Convertfly · renderizador de cards 4:5
  Um browser para todos os cards. Screenshot do elemento .slide, nao do
  viewport: garante 1080 x 1350 exatos, sem faixa de fundo sobrando.

  node render.js <pastaHTML> <pastaPNG>
*/
const { chromium } = require('playwright-core');
const fs = require('fs');
const path = require('path');

const LARGURA = 1080, ALTURA = 1350;

function acharChrome() {
  const base = '/opt/pw-browsers';
  const dirs = fs.readdirSync(base).filter(d => d.startsWith('chromium-')).sort();
  if (!dirs.length) throw new Error('Chromium nao encontrado');
  return path.join(base, dirs[dirs.length - 1], 'chrome-linux', 'chrome');
}

(async () => {
  const [entrada, saida] = process.argv.slice(2);
  fs.mkdirSync(saida, { recursive: true });

  const browser = await chromium.launch({ executablePath: acharChrome(), args: ['--no-sandbox'] });
  const page = await browser.newPage({
    viewport: { width: LARGURA, height: ALTURA },
    deviceScaleFactor: 1,
  });

  const arquivos = fs.readdirSync(entrada).filter(f => /^card-\d+\.html$/.test(f)).sort();
  for (const arq of arquivos) {
    await page.goto('file://' + path.join(entrada, arq));
    await page.evaluate(() => document.fonts.ready);
    const alvo = page.locator('.slide');
    const box = await alvo.boundingBox();
    if (Math.round(box.width) !== LARGURA || Math.round(box.height) !== ALTURA) {
      throw new Error(`${arq}: slide em ${box.width}x${box.height}, esperado ${LARGURA}x${ALTURA}`);
    }
    const png = arq.replace('.html', '.png');
    await alvo.screenshot({ path: path.join(saida, png) });
    console.log('  ' + png);
  }

  await browser.close();
})().catch(e => { console.error(e.message); process.exit(1); });
