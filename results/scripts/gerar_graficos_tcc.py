import os
import matplotlib.pyplot as plt
import numpy as np

# Cria o diretório de destino na raiz do repositório
output_dir = os.path.join("results", "figures")
os.makedirs(output_dir, exist_ok=True)

# Tipografia e cores padrão
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#2E2E2E'
plt.rcParams['axes.labelcolor'] = '#2E2E2E'
plt.rcParams['xtick.color'] = '#2E2E2E'
plt.rcParams['ytick.color'] = '#2E2E2E'

# ==============================================================================
# FIGURA 1: Gráfico de Barras SUS Individual vs. Escala Bangor
# ==============================================================================
participantes = [
    'P1 (Geovana)', 
    'P2 (Josiane)', 
    'P3 (Amabili)', 
    'P4 (Beatriz)', 
    'P5 (Sabrina)', 
    'P6 (Milena)'
]
scores = [95.0, 100.0, 80.0, 92.5, 97.5, 95.0]
media_sus = np.mean(scores)  # 93.33

fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)

# Zonas de Aceitabilidade (Bangor et al., 2008/2009)
ax.axhspan(80.3, 105, color='#D4EDDA', alpha=0.5, label='Grau A / Excelente (≥ 80.3)')
ax.axhspan(68.0, 80.3, color='#FFF3CD', alpha=0.5, label='Grau B/C / Aceitável (68.0 a 80.2)')
ax.axhline(68.0, color='#E0A800', linestyle='--', linewidth=1.2, label='Média Literatura (68.0)')
ax.axhline(media_sus, color='#D9534F', linestyle='-', linewidth=2, label=f'Média Rede Delas ({media_sus:.1f})')

# Barras
barras = ax.bar(participantes, scores, color='#F39C5A', width=0.55, edgecolor='#E67E22', linewidth=1.2, zorder=3)

for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura:.1f}',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 4),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold', color='#2E2E2E')

ax.set_title('Pontuação Individual do SUS e Zona de Aceitabilidade', fontsize=14, pad=15, fontweight='bold')
ax.set_ylabel('Pontuação SUS (0 - 100)', fontsize=11, labelpad=10)
ax.set_ylim(0, 108)
ax.set_yticks(np.arange(0, 101, 10))
ax.grid(axis='y', linestyle=':', alpha=0.6, zorder=0)
ax.legend(loc='lower right', frameon=True, facecolor='white', framealpha=0.9, fontsize=9)

plt.tight_layout()
caminho_fig1 = os.path.join(output_dir, 'grafico_sus_individual.png')
plt.savefig(caminho_fig1, dpi=300)
plt.close()
print(f"Figura 1 salva: {caminho_fig1}")

# ==============================================================================
# FIGURA 2: Gráfico Radar por Questão do SUS
# ==============================================================================
labels = [
    'Q1. Frequência\nde uso',
    'Q2. Complexidade\ndesnecessária (*)',
    'Q3. Facilidade\nde uso',
    'Q4. Suporte\ntécnico (*)',
    'Q5. Integração\ndas funções',
    'Q6. Inconsistência\npercebida (*)',
    'Q7. Aprendizado\nrápido',
    'Q8. Muito\ncomplicado (*)',
    'Q9. Confiança\nno uso',
    'Q10. Necessidade\nde pré-treino (*)'
]

medias = [5.0, 1.0, 4.83, 1.67, 4.83, 1.83, 4.5, 1.0, 4.83, 1.0]

num_vars = len(labels)
angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
medias_radar = medias + [medias[0]]
angulos_radar = angulos + [angulos[0]]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), dpi=300)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angulos, labels, color='#2E2E2E', size=9, weight='bold')
ax.set_rscale('linear')
plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="#7F8C8D", size=9)
plt.ylim(0, 5.3)

ax.plot(angulos_radar, medias_radar, color='#F39C5A', linewidth=2, linestyle='solid')
ax.fill(angulos_radar, medias_radar, color='#F39C5A', alpha=0.35)

ax.set_title('Médias do SUS por Questão (Escala Likert 1-5)\n(*) Questões com polaridade negativa', 
             size=13, weight='bold', pad=25)

plt.tight_layout()
caminho_fig2 = os.path.join(output_dir, 'grafico_sus_radar.png')
plt.savefig(caminho_fig2, dpi=300)
plt.close()
print(f"Figura 2 salva: {caminho_fig2}")