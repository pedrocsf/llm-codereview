import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Patch

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PREVIEW_DIR = "/tmp/claude-1000/-home-pedro-Github-llm-codereview/76f37ea0-6a84-4720-8d70-412baaf7b301/scratchpad/survey_previews"
NAMES = ["taxonomy", "benchmarks", "pipeline", "field_outcomes"]

BLUE = "#0072B2"
ORANGE = "#E69F00"
GREEN = "#009E73"
VERMILION = "#D55E00"
GRAY = "#666666"
LIGHT = "#E8EEF4"
NEWFILL = "#FCE9C2"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Liberation Serif", "Nimbus Roman", "Times New Roman", "DejaVu Serif"],
    "font.size": 7,
    "axes.labelsize": 7,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 6.5,
    "pdf.fonttype": 42,
    "axes.linewidth": 0.6,
})

TEXT = {
    "en": {
        "dec": ".",
        "tax_dims": [
            ("D1", "Review task", "necessity, comment generation, defect detection, refinement, triage, evaluation"),
            ("D2", "Model adaptation", "pre-training, fine-tuning, PEFT, prompting, RAG, RL, data-centric, distillation"),
            ("D3", "System architecture", "single call, generator + filter, multi-agent, tool-using, hybrid with static analysis"),
            ("D4", "Context scope", "hunk, function/slice, file, cross-file/repository, non-code intent"),
            ("D5", "Evaluation regime", "text similarity, LLM judge, issue-level P/R, tests, field outcomes, RCTs"),
            ("D6", "Deployment and cost", "frontier API, self-hosted, small/local, cascade/routing, cost reported or not"),
            ("D7", "Trust and risk", "precision control, hallucination, adversarial robustness, human factors, privacy"),
        ],
        "tax_new": "new",
        "tax_note": "D6 and D7 are the main additions over prior task-centred taxonomies.",
        "bm_a": "(a) Synthetic to real collapse",
        "bm_a_groups": ["Kumar et al. 2026", "PrimeVul (7B)"],
        "bm_a_series": ["Synthetic / BigVul", "Real PRs / PrimeVul"],
        "bm_a_ylabel": "F1 (%)",
        "bm_b": "(b) Best results on real-PR benchmarks",
        "bm_b_rows": [
            ("SWR-Bench", "F1", "19.38"),
            ("SWR-Bench, Self-Agg n=10", "F1", "21.91"),
            ("AACR-Bench", "F1", "16.12"),
            ("SWE-PRBench", "issues detected", "15–31"),
            ("CR-Bench-v2", "known-defect detection", "≈33"),
            ("c-CRAB (Claude Code)", "test pass rate", "32.1"),
        ],
        "bm_b_xlabel": "Reported value (%)",
        "bm_b_legend": ["F1", "Issue/defect detection rate", "Test pass rate"],
        "bm_note": "Metrics, datasets and judges differ across studies; values are not directly comparable.",
        "pl_stages": ["PR\n(diff + metadata)", "Context\nbuilder", "LLM\ngenerator", "Filter /\nverifier", "Ranker /\nthreshold", "Developer"],
        "pl_sub": [
            "",
            "slicing,\nretrieval, intent",
            "broad candidate\ncomments",
            "LLM judge,\nclassifier, consensus,\nstatic checks",
            "top-k, confidence\ncutoff",
            "",
        ],
        "pl_examples": ["", "RovoDev", "ICML 2025", "BitsAI-CR\nICML 2025", "AutoCommenter", ""],
        "pl_banner_left": "generate broadly",
        "pl_banner_right": "filter rigorously",
        "pl_feedback": "feedback: accepted / rejected / resolved comments",
        "pl_ex_title": "Example systems",
    },
    "ptbr": {
        "dec": ",",
        "tax_dims": [
            ("D1", "Tarefa de revisão", "necessidade, geração de comentários, detecção de defeitos, refinamento, triagem"),
            ("D2", "Adaptação do modelo", "pré-treino, ajuste fino, PEFT, prompting, RAG, RL, centrada em dados, destilação"),
            ("D3", "Arquitetura do sistema", "chamada única, gerador + filtro, multiagente, ferramentas, híbrido com análise estática"),
            ("D4", "Escopo de contexto", "trecho, função/slice, arquivo, multiarquivo/repositório, intenção não código"),
            ("D5", "Regime de avaliação", "similaridade textual, juiz LLM, P/R por problema, testes, resultados em campo, RCTs"),
            ("D6", "Implantação e custo", "API de fronteira, auto-hospedado, pequeno/local, cascata, custo reportado ou não"),
            ("D7", "Confiança e risco", "controle de precisão, alucinação, robustez adversarial, fatores humanos, privacidade"),
        ],
        "tax_new": "nova",
        "tax_note": "D6 e D7 são as principais adições em relação às taxonomias centradas em tarefas.",
        "bm_a": "(a) Colapso do sintético ao real",
        "bm_a_groups": ["Kumar et al. 2026", "PrimeVul (7B)"],
        "bm_a_series": ["Sintético / BigVul", "PRs reais / PrimeVul"],
        "bm_a_ylabel": "F1 (%)",
        "bm_b": "(b) Melhores resultados em benchmarks de PRs reais",
        "bm_b_rows": [
            ("SWR-Bench", "F1", "19,38"),
            ("SWR-Bench, Self-Agg n=10", "F1", "21,91"),
            ("AACR-Bench", "F1", "16,12"),
            ("SWE-PRBench", "problemas detectados", "15–31"),
            ("CR-Bench-v2", "detecção de defeitos conhecidos", "≈33"),
            ("c-CRAB (Claude Code)", "taxa de aprovação nos testes", "32,1"),
        ],
        "bm_b_xlabel": "Valor reportado (%)",
        "bm_b_legend": ["F1", "Taxa de detecção de problemas/defeitos", "Taxa de aprovação nos testes"],
        "bm_note": "Métricas, conjuntos de dados e juízes diferem entre estudos; valores não são diretamente comparáveis.",
        "pl_stages": ["PR\n(diff + metadados)", "Construtor\nde contexto", "Gerador\nLLM", "Filtro /\nverificador", "Ranqueador /\nlimiar", "Desenvolvedor"],
        "pl_sub": [
            "",
            "slicing,\nrecuperação,\nintenção",
            "comentários\ncandidatos em\nabundância",
            "juiz LLM,\nclassificador, consenso,\nchecagem estática",
            "top-k, corte de\nconfiança",
            "",
        ],
        "pl_examples": ["", "RovoDev", "ICML 2025", "BitsAI-CR\nICML 2025", "AutoCommenter", ""],
        "pl_banner_left": "gerar amplamente",
        "pl_banner_right": "filtrar com rigor",
        "pl_feedback": "feedback: comentários aceitos / rejeitados / resolvidos",
        "pl_ex_title": "Sistemas de exemplo",
    },
}

FIELD = {
    "en": {
        "rows": [
            ("Atlassian (RovoDev)", 38.70, "res", "38.70", (44.45, 44.45), "44.45"),
            ("ByteDance (BitsAI-CR)", 26.7, "out", "26.7", (35, 46), "35–46"),
            ("Google (AutoCommenter)", 40, "res", "~40", None, ""),
            ("Meta (MetaMateCR)", 19.7, "app", "19.7", None, ""),
            ("CodeRabbit (OSS)", 36.4, "acc", "36.4", None, ""),
            ("Mozilla (RevMate)", 8.1, "acc", "8.1", None, ""),
            ("Ubisoft (RevMate)", 7.2, "acc", "7.2", None, ""),
            ("Beko (PR-Agent)", 73.8, "lab", "73.8", None, ""),
        ],
        "kinds": {
            "res": "Comment resolution rate",
            "out": "Outdated Rate (lower is better)",
            "app": "Patches applied",
            "acc": "Comments accepted",
            "lab": "Author-set \"Resolved\" label (mandatory)",
        },
        "human": "Human baseline",
        "xlabel": "Reported value (%)",
        "note": "Outcome metrics are defined differently by each organisation and are not directly comparable.",
        "dec": ".",
    },
    "ptbr": {
        "rows": [
            ("Atlassian (RovoDev)", 38.70, "res", "38,70", (44.45, 44.45), "44,45"),
            ("ByteDance (BitsAI-CR)", 26.7, "out", "26,7", (35, 46), "35–46"),
            ("Google (AutoCommenter)", 40, "res", "~40", None, ""),
            ("Meta (MetaMateCR)", 19.7, "app", "19,7", None, ""),
            ("CodeRabbit (OSS)", 36.4, "acc", "36,4", None, ""),
            ("Mozilla (RevMate)", 8.1, "acc", "8,1", None, ""),
            ("Ubisoft (RevMate)", 7.2, "acc", "7,2", None, ""),
            ("Beko (PR-Agent)", 73.8, "lab", "73,8", None, ""),
        ],
        "kinds": {
            "res": "Taxa de resolução de comentários",
            "out": "Outdated Rate (menor é melhor)",
            "app": "Patches aplicados",
            "acc": "Comentários aceitos",
            "lab": "Rótulo \"Resolvido\" do autor (obrigatório)",
        },
        "human": "Baseline humano",
        "xlabel": "Valor reportado (%)",
        "note": "As métricas são definidas de forma diferente por cada organização e não são diretamente comparáveis.",
        "dec": ",",
    },
}


def box(ax, x, y, w, h, fc, ec, lw=0.8, ls="-", rounding=0.04):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={rounding}",
                       fc=fc, ec=ec, lw=lw, ls=ls)
    ax.add_patch(p)
    return p


def fig_taxonomy(lang):
    t = TEXT[lang]
    fig, ax = plt.subplots(figsize=(6.3, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.1)
    ax.axis("off")
    rows = t["tax_dims"]
    n = len(rows)
    h = 0.92
    gap = 0.17
    for i, (code, name, cats) in enumerate(rows):
        y = 8.1 - 0.15 - (i + 1) * h - i * gap
        new = code in ("D6", "D7")
        box(ax, 0, y, 3.0, h, ORANGE if new else BLUE, "none")
        ax.text(0.15, y + h / 2 + (0.08 if new else 0), f"{code}  {name}", ha="left", va="center",
                color="black" if new else "white", fontsize=8, fontweight="bold")
        box(ax, 3.1, y, 6.9, h, NEWFILL if new else LIGHT,
            ORANGE if new else BLUE, lw=0.8 if new else 0.5)
        ax.text(3.25, y + h / 2, cats, ha="left", va="center", fontsize=6.5)
        if new:
            ax.text(2.9, y + 0.06, t["tax_new"], ha="right", va="bottom",
                    fontsize=6, style="italic", color="black")
    ax.text(0, 0.0, t["tax_note"], ha="left", va="center", fontsize=6.5, style="italic", color=GRAY)
    return fig


def fig_benchmarks(lang):
    t = TEXT[lang]
    dec = t["dec"]
    fig, (a, b) = plt.subplots(1, 2, figsize=(6.3, 2.9), gridspec_kw={"width_ratios": [1, 1.5], "wspace": 0.8})
    vals = [[84.7, 6.6], [68.26, 3.09]]
    labs = [["0" + dec + "847", "0" + dec + "066"], ["68" + dec + "26", "3" + dec + "09"]]
    cols = [BLUE, VERMILION]
    hatches = ["", "///"]
    w = 0.38
    for s in range(2):
        xs = [g + (s - 0.5) * w for g in range(2)]
        ys = [vals[g][s] for g in range(2)]
        bars = a.bar(xs, ys, w, color=cols[s], hatch=hatches[s], edgecolor="white" if s == 0 else "white",
                     lw=0.4, label=t["bm_a_series"][s])
        for x, y, g in zip(xs, ys, range(2)):
            a.text(x, y + 1.5, labs[g][s], ha="center", va="bottom", fontsize=6.5)
    a.set_xticks(range(2))
    a.set_xticklabels([g.replace(" (", "\n(").replace(" et al. ", " et al.\n") for g in t["bm_a_groups"]], fontsize=6.5)
    a.set_ylim(0, 118)
    a.set_yticks(range(0, 101, 20))
    a.set_ylabel(t["bm_a_ylabel"])
    a.set_title(t["bm_a"], fontsize=7.5, loc="left")
    a.legend(loc="upper right", frameon=False, fontsize=6.3, handlelength=1.2)
    for sp in ("top", "right"):
        a.spines[sp].set_visible(False)

    rows = t["bm_b_rows"]
    n = len(rows)
    numeric = [19.38, 21.91, 16.12, None, 33, 32.1]
    kinds = [0, 0, 0, 1, 1, 2]
    kcol = [BLUE, GREEN, ORANGE]
    khatch = ["", "..", "\\\\"]
    for i, ((name, metric, lab), v, k) in enumerate(zip(rows, numeric, kinds)):
        y = n - 1 - i
        if v is None:
            b.barh(y, 31 - 15, left=15, height=0.55, color=kcol[k], hatch=khatch[k], edgecolor="white", lw=0.4)
            b.text(31.8, y, lab, va="center", fontsize=6.5)
        else:
            b.barh(y, v, height=0.55, color=kcol[k], hatch=khatch[k], edgecolor="white", lw=0.4)
            b.text(v + 0.8, y, lab, va="center", fontsize=6.5)
    b.set_yticks(range(n))
    b.set_yticklabels([r[0] for r in rows][::-1], fontsize=6.5)
    b.set_xlim(0, 42)
    b.set_xlabel(t["bm_b_xlabel"])
    b.set_title(t["bm_b"], fontsize=7.5, loc="left")
    for sp in ("top", "right"):
        b.spines[sp].set_visible(False)
    handles = [Patch(fc=kcol[k], hatch=khatch[k], ec="white", label=t["bm_b_legend"][k]) for k in range(3)]
    b.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.4, -0.2), ncol=1, frameon=False, fontsize=6.3, handlelength=1.2)
    fig.text(0.5, -0.27, t["bm_note"], ha="center", va="top", fontsize=6.5, style="italic", color=GRAY)
    return fig


def fig_pipeline(lang):
    t = TEXT[lang]
    fig, ax = plt.subplots(figsize=(6.3, 3.2))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    n = 6
    bw, gap = 1.7, 0.35
    y0, bh = 3.3, 1.2
    fills = [LIGHT, LIGHT, "#CFE3F2", NEWFILL, NEWFILL, LIGHT]
    edges = [GRAY, BLUE, BLUE, ORANGE, ORANGE, GRAY]
    xs = [0.05 + i * (bw + gap) for i in range(n)]
    for i in range(n):
        box(ax, xs[i], y0, bw, bh, fills[i], edges[i], lw=1.0)
        ax.text(xs[i] + bw / 2, y0 + bh / 2, t["pl_stages"][i], ha="center", va="center",
                fontsize=7.5, fontweight="bold", linespacing=1.15)
        if t["pl_sub"][i]:
            ax.text(xs[i] + bw / 2, y0 - 0.2, t["pl_sub"][i], ha="center", va="top",
                    fontsize=6.3, linespacing=1.1, color="#222222")
        if t["pl_examples"][i]:
            ax.text(xs[i] + bw / 2, y0 - 1.45, t["pl_examples"][i], ha="center", va="top",
                    fontsize=7, style="italic", color=VERMILION, linespacing=1.15)
        if i < n - 1:
            ax.add_patch(FancyArrowPatch((xs[i] + bw + 0.02, y0 + bh / 2), (xs[i + 1] - 0.02, y0 + bh / 2),
                                         arrowstyle="-|>", mutation_scale=7, lw=1.0, color="black"))
    span_y = y0 + bh + 0.35
    ax.annotate("", xy=(xs[2] + bw, span_y), xytext=(xs[1], span_y),
                arrowprops=dict(arrowstyle="-", lw=0.8, color=BLUE))
    ax.text((xs[1] + xs[2] + bw) / 2, span_y + 0.12, t["pl_banner_left"], ha="center", va="bottom",
            fontsize=7, color=BLUE, fontweight="bold")
    ax.annotate("", xy=(xs[4] + bw, span_y), xytext=(xs[3], span_y),
                arrowprops=dict(arrowstyle="-", lw=0.8, color=ORANGE))
    ax.text((xs[3] + xs[4] + bw) / 2, span_y + 0.12, t["pl_banner_right"], ha="center", va="bottom",
            fontsize=7, color="#8a5a00", fontweight="bold")
    fy = 0.55
    ax.plot([xs[5] + bw / 2, xs[5] + bw / 2], [y0, fy], color=GRAY, lw=0.9, ls=(0, (4, 2)))
    ax.plot([xs[5] + bw / 2, xs[0] + bw / 2], [fy, fy], color=GRAY, lw=0.9, ls=(0, (4, 2)))
    ax.add_patch(FancyArrowPatch((xs[0] + bw / 2, fy), (xs[0] + bw / 2, y0 - 0.02),
                                 arrowstyle="-|>", mutation_scale=7, lw=0.9, color=GRAY, ls=(0, (4, 2))))
    ax.text((xs[5] + xs[0] + bw) / 2, fy + 0.12, t["pl_feedback"], ha="center", va="bottom",
            fontsize=6.5, style="italic", color=GRAY,
            bbox=dict(fc="white", ec="none", pad=1.0))
    return fig


def fig_field(lang):
    t = FIELD[lang]
    dec = t["dec"]
    fig, ax = plt.subplots(figsize=(6.3, 3.0))
    style = {
        "res": ("o", BLUE),
        "out": ("s", VERMILION),
        "app": ("D", GREEN),
        "acc": ("^", ORANGE),
        "lab": ("*", "black"),
    }
    rows = t["rows"]
    n = len(rows)
    used = []
    for i, (org, v, kind, lab, hum, hlab) in enumerate(rows):
        y = n - 1 - i
        m, c = style[kind]
        ax.hlines(y, 0, v, color=c, lw=1.0, alpha=0.7)
        ax.plot(v, y, marker=m, color=c, ms=8 if m == "*" else 5.5, mec="black", mew=0.4, zorder=3,
                label=t["kinds"][kind] if kind not in used else None)
        if kind not in used:
            used.append(kind)
        if hum is not None:
            if hum[0] == hum[1]:
                ax.plot(hum[0], y, marker="|", color="black", ms=10, mew=1.4, zorder=3,
                        label=t["human"] if "h" not in used else None)
            else:
                ax.plot(hum, [y, y], color="black", lw=2.2, solid_capstyle="butt", zorder=3,
                        label=t["human"] if "h" not in used else None)
            if "h" not in used:
                used.append("h")
            ax.text(hum[1] + 1.2, y, hlab, va="center", fontsize=6.3, color="black")
            ax.text(v - 1.5, y + 0.33, lab + "%", va="bottom", ha="right", fontsize=6.5)
        else:
            ax.text(v + 2, y, lab + "%", va="center", fontsize=6.5)
    ax.set_yticks(range(n))
    ax.set_yticklabels([r[0] for r in rows][::-1])
    ax.set_xlim(0, 85)
    ax.set_ylim(-0.7, n - 0.3)
    ax.set_xlabel(t["xlabel"])
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.grid(axis="x", lw=0.3, color="#cccccc")
    ax.set_axisbelow(True)
    h, l = ax.get_legend_handles_labels()
    ax.legend(h, l, loc="center right", bbox_to_anchor=(1.0, 0.6), frameon=False, fontsize=6.5, handlelength=1.4, labelspacing=0.35)
    fig.text(0.5, -0.01, t["note"], ha="center", va="top", fontsize=6.5, style="italic", color=GRAY)
    return fig


BUILDERS = {
    "taxonomy": fig_taxonomy,
    "benchmarks": fig_benchmarks,
    "pipeline": fig_pipeline,
    "field_outcomes": fig_field,
}


def main():
    os.makedirs(PREVIEW_DIR, exist_ok=True)
    for lang in ("en", "ptbr"):
        outdir = os.path.join(ROOT, lang, "figures")
        os.makedirs(outdir, exist_ok=True)
        for name in NAMES:
            fig = BUILDERS[name](lang)
            fig.savefig(os.path.join(outdir, name + ".pdf"), bbox_inches="tight")
            fig.savefig(os.path.join(PREVIEW_DIR, f"{lang}_{name}.png"), dpi=110, bbox_inches="tight")
            plt.close(fig)


if __name__ == "__main__":
    main()
