import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# Cria o diretório de destino na raiz do repositório
output_dir = os.path.join("results", "figures")
os.makedirs(output_dir, exist_ok=True)

# Tipografia e cores padrão
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#1E1A3C' # Text/Primário do Design System
plt.rcParams['axes.labelcolor'] = '#1E1A3C'
plt.rcParams['xtick.color'] = '#1E1A3C'
plt.rcParams['ytick.color'] = '#1E1A3C'

# AJUSTE v2: opções simples (True/False)
MOSTRAR_TITULO = True            # False se o título ficar só na legenda do TCC
GERAR_BARRAS_ALTERNATIVA = True  # gera também a Figura 3 (alternativa ao radar)

def virgula(x, casas=1):
    """Número com vírgula decimal (padrão do texto em português)."""
    return f"{x:.{casas}f}".replace('.', ',')

# ==============================================================================
# DADOS: respostas brutas do SUS (1 a 5). Somente códigos, sem nomes.
# AJUSTE v2: as notas e as médias por questão são CALCULADAS daqui (antes eram digitadas,
# o que permitiu o erro do Q5 = 4,83; o correto é 4,67).
# ==============================================================================
participantes = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']
perfis = ['Mentora', 'Gestão', 'Mentoranda', 'Mentora', 'Gestão', 'Mentoranda']
cores_perfil = {'Mentoranda': '#D4537E', 'Mentora': '#6C4CF1', 'Gestão': '#2EC4B6'}  # Style Guide

respostas = np.array([
    [5, 1, 5, 1, 4, 1, 4, 1, 5, 1],   # P1
    [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],   # P2
    [5, 1, 5, 5, 5, 5, 5, 1, 5, 1],   # P3
    [5, 1, 4, 1, 5, 1, 4, 1, 4, 1],   # P4
    [5, 1, 5, 1, 5, 1, 4, 1, 5, 1],   # P5
    [5, 1, 5, 1, 4, 2, 5, 1, 5, 1],   # P6
])

# Contribuição de cada item (0 a 4): ímpares = resposta - 1; pares = 5 - resposta (Brooke, 1996)
contribuicao = np.where(np.arange(10) % 2 == 0, respostas - 1, 5 - respostas)
scores = contribuicao.sum(axis=1) * 2.5
media_sus = np.mean(scores)  # 93.33
dp_sus = np.std(scores, ddof=1)
t_crit = 2.5706              # t de Student, 95% bilateral, 5 graus de liberdade (n = 6)
ic_inf = media_sus - t_crit * dp_sus / np.sqrt(len(scores))
ic_sup = min(100, media_sus + t_crit * dp_sus / np.sqrt(len(scores)))  # limitado a 100 (máximo da escala)
contrib_media = contribuicao.mean(axis=0)

# Conferência com as notas já usadas no texto (evita erro de digitação)
assert list(scores) == [95.0, 100.0, 80.0, 92.5, 97.5, 95.0], "notas diferentes das conferidas"

# ==============================================================================
# FIGURA 1: Gráfico de Barras SUS Individual vs. Escala Bangor
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# Zonas de referência (mantidas). AJUSTE v2: vão só até 100, o máximo da escala
ax.axhspan(80.3, 100, color='#DCFCE7', alpha=0.5, zorder=0)   # Estado/Fundo Sucesso
ax.axhspan(68.0, 80.3, color='#FEF3C7', alpha=0.5, zorder=0)  # Estado/Fundo Neutro
ax.axhline(68.0, color='#F59E0B', linestyle='--', linewidth=1.2)  # Estado/Atenção
# AJUSTE v2: faixa do intervalo de confiança de 95% da média
ax.axhspan(ic_inf, ic_sup, color='#2D1B6E', alpha=0.08, zorder=1)
# AJUSTE v2: média em roxo-noite (o turquesa agora identifica o perfil Gestão)
ax.axhline(media_sus, color='#2D1B6E', linestyle='-', linewidth=2, zorder=2)

# Barras. AJUSTE v2: uma cor por perfil
barras = ax.bar(participantes, scores, color=[cores_perfil[p] for p in perfis], width=0.55, zorder=3)

for barra in barras:
    altura = barra.get_height()
    ax.annotate(virgula(altura),
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 4),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=11, fontweight='bold', color='#1E1A3C')

# AJUSTE v2: indica quem fica abaixo do corte de 80,3 (P3 = 80,0)
for i, v in enumerate(scores):
    if v < 80.3:
        ax.text(i, v * 0.70, f"{virgula(80.3 - v)} abaixo\nde 80,3", ha='center', va='center',
                fontsize=9, color='white', fontweight='bold', zorder=4)

if MOSTRAR_TITULO:
    ax.set_title('Pontuação Individual do SUS e Zona de Aceitabilidade', fontsize=14, pad=15, fontweight='bold')
ax.set_ylabel('Pontuação SUS (0 a 100)', fontsize=11, labelpad=10)
ax.set_xticks(range(len(participantes)))
ax.set_xticklabels([f"{c}\n{p}" for c, p in zip(participantes, perfis)], fontsize=10)  # AJUSTE v2: perfil no eixo
ax.set_ylim(0, 106)
ax.set_yticks(np.arange(0, 101, 10))
ax.grid(axis='y', linestyle=':', alpha=0.6, zorder=0)
for lado in ('top', 'right'):
    ax.spines[lado].set_visible(False)

# AJUSTE v2: legenda ABAIXO do gráfico (antes cobria as barras de P5 e P6) e rótulos corrigidos
legenda = [Patch(color=cores_perfil[k], label=k) for k in cores_perfil] + [
    Line2D([0], [0], color='#2D1B6E', lw=2, label=f'Média do protótipo ({virgula(media_sus)})'),
    Patch(color='#2D1B6E', alpha=0.12, label=f'IC 95% da média ({virgula(ic_inf)} a {virgula(ic_sup)})'),
    Patch(color='#DCFCE7', alpha=0.8, label='Zona do conceito A (≥ 80,3)'),
    Patch(color='#FEF3C7', alpha=0.8, label='Zona aceitável (68 a 80,3)'),
    Line2D([0], [0], color='#F59E0B', ls='--', lw=1.2, label='Média global do SUS (68)'),  # antes: "Média Literatura"
]
ax.legend(handles=legenda, loc='upper center', bbox_to_anchor=(0.5, -0.14), ncol=4, frameon=False, fontsize=9)

plt.tight_layout()
caminho_fig1 = os.path.join(output_dir, 'grafico_sus_individual.png')
plt.savefig(caminho_fig1, dpi=300, bbox_inches='tight')
plt.savefig(caminho_fig1.replace('.png', '.pdf'), bbox_inches='tight')  # AJUSTE v2: versão vetorial
plt.close()
print(f"Figura 1 salva: {caminho_fig1}")

# ==============================================================================
# FIGURA 2: Gráfico Radar por Questão do SUS
# AJUSTE v2: o radar passa a mostrar a CONTRIBUIÇÃO (0 a 4) e não a média bruta (1 a 5).
# Motivo: na média bruta, itens positivos ficam perto de 5 e negativos perto de 1, e a "estrela"
# é só efeito dessa alternância. Na contribuição, quanto mais longe do centro, melhor, em todos os eixos.
# ==============================================================================
labels = [
    'Q1. Usaria com\nfrequência',
    'Q2. Complexidade\ndesnecessária (*)',
    'Q3. Fácil\nde usar',
    'Q4. Precisaria de\najuda técnica (*)',          # antes: "Suporte técnico"
    'Q5. Funções\nbem integradas',
    'Q6. Muita\ninconsistência (*)',
    'Q7. Aprendizado\nrápido',
    'Q8. Muito\ncomplicado (*)',
    'Q9. Confiança\nno uso',
    'Q10. Aprender muito\nantes de usar (*)'         # antes: "Necessidade de pré-treino"
]

medias = list(contrib_media)  # [4.00, 4.00, 3.83, 3.33, 3.67, 3.17, 3.50, 4.00, 3.83, 4.00]

num_vars = len(labels)
angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
medias_radar = medias + [medias[0]]
angulos_radar = angulos + [angulos[0]]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), dpi=300)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angulos, labels, color='#1E1A3C', size=9, weight='bold') # Text/Primário
ax.tick_params(axis='x', pad=14)                                      # AJUSTE v2: afasta os rótulos do gráfico
ax.set_rscale('linear')
plt.yticks([1, 2, 3, 4], ["1", "2", "3", "4"], color="#8B7EB8", size=9) # Text/Muted
plt.ylim(0, 4.4)
ax.set_rlabel_position(18)  # AJUSTE v2: números do eixo entre dois eixos (não colam em Q2)

ax.plot(angulos_radar, medias_radar, color='#6C4CF1', linewidth=2, linestyle='solid') # Roxo/Primário
ax.fill(angulos_radar, medias_radar, color='#6C4CF1', alpha=0.35) # Roxo/Primário translúcido
for ang, v in zip(angulos, medias):  # AJUSTE v2: valor em cada vértice
    ax.text(ang, v - 0.38, virgula(v, 2), ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1E1A3C')

if MOSTRAR_TITULO:
    ax.set_title('Contribuição média de cada afirmação do SUS (0 a 4)\n(*) afirmação negativa, já invertida: quanto maior, melhor',
                 size=13, weight='bold', pad=40)

plt.tight_layout()
caminho_fig2 = os.path.join(output_dir, 'grafico_sus_radar.png')
plt.savefig(caminho_fig2, dpi=300, bbox_inches='tight')
plt.savefig(caminho_fig2.replace('.png', '.pdf'), bbox_inches='tight')
plt.close()
print(f"Figura 2 salva: {caminho_fig2}")

# ==============================================================================
# FIGURA 3 (OPCIONAL): mesma informação da Figura 2 em barras horizontais, mais fácil de ler valor a valor
# ==============================================================================
if GERAR_BARRAS_ALTERNATIVA:
    itens = ["Usaria o sistema com frequência (+)", "Sistema desnecessariamente complexo (−)", "Fácil de usar (+)",
             "Precisaria de ajuda técnica (−)", "Funções bem integradas (+)", "Muita inconsistência (−)",
             "Maioria aprenderia rapidamente (+)", "Muito complicado de usar (−)", "Senti-me confiante (+)",
             "Precisei aprender muito antes de usar (−)"]
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    y = np.arange(10)[::-1]
    cores = ['#6C4CF1' if i % 2 == 0 else '#2EC4B6' for i in range(10)]
    ax.barh(y, contrib_media, color=cores, height=0.6, zorder=3)
    for yy, v in zip(y, contrib_media):
        ax.text(v + 0.04, yy, virgula(v, 2), va='center', fontsize=10, fontweight='bold')
    ax.set_yticks(y)
    ax.set_yticklabels([f"Q{i + 1}  {t}" for i, t in enumerate(itens)], fontsize=9.5)
    ax.set_xlim(0, 4.4)
    ax.set_xticks(range(0, 5))
    ax.set_xlabel('Contribuição média à pontuação (0 a 4; 4 = melhor resultado possível)', fontsize=10.5)
    ax.grid(axis='x', linestyle=':', alpha=0.6, zorder=0)
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)
    ax.legend(handles=[Patch(color='#6C4CF1', label='Afirmação positiva (+): resposta − 1'),
                       Patch(color='#2EC4B6', label='Afirmação negativa (−): 5 − resposta')],
              loc='upper center', bbox_to_anchor=(0.5, -0.13), ncol=2, frameon=False, fontsize=9)
    plt.tight_layout()
    caminho_fig3 = os.path.join(output_dir, 'grafico_sus_itens_barras.png')
    plt.savefig(caminho_fig3, dpi=300, bbox_inches='tight')
    plt.savefig(caminho_fig3.replace('.png', '.pdf'), bbox_inches='tight')
    plt.close()
    print(f"Figura 3 (opcional) salva: {caminho_fig3}")

# ==============================================================================
# RESUMO NO TERMINAL (números usados no texto do TCC)
# ==============================================================================
print(f"Notas: {[virgula(v) for v in scores]}")
print(f"Média {virgula(media_sus, 2)} | DP {virgula(dp_sus, 2)} | IC95% [{virgula(ic_inf)}; {virgula(ic_sup)}]")
print(f"Contribuição por questão: {[virgula(v, 2) for v in contrib_media]}")