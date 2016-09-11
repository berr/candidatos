import pandas
import matplotlib.pyplot as plt


def print_full(x):
    with pandas.option_context('display.max_rows', len(x), 'display.max_columns', len(x.columns)):
        print(x)

columns = [
    "DATA_GERACAO", "HORA_GERACAO", "ANO_ELEICAO", "NUM_TURNO", "DESCRICAO_ELEICAO", "SIGLA_UF", "SIGLA_UE",
    "DESCRICAO_UE", "CODIGO_CARGO", "DESCRICAO_CARGO", "NOME_CANDIDATO", "SEQUENCIAL_CANDIDATO", "NUMERO_CANDIDATO",
    "CPF_CANDIDATO", "NOME_URNA_CANDIDATO", "COD_SITUACAO_CANDIDATURA", "DES_SITUACAO_CANDIDATURA",
    "NUMERO_PARTIDO", "SIGLA_PARTIDO", "NOME_PARTIDO", "CODIGO_LEGENDA", "SIGLA_LENDA", "COMPOSICAO_LEGENDA",
    "NOME_LEGENDA", "CODIGO_OCUPACAO", "DESCRICAO_OCUPACAO", "DATA_NASCIMENTO", "NUM_TITULO_ELEITORAL_CANDIDATO",
    "IDADE_DATA_ELEICAO", "CODIGO_SEXO", "DESCRICAO_SEXO", "COD_GRAU_INSTRUCAO", "DESCRICAO_GRAU_INSTRUCAO",
    "CODIGO_ESTADO_CIVIL", "DESCRICAO_ESTADO_CIVIL", "CODIGO_COR_RACA", "DESCRICAO_COR_RACA",
    "CODIGO_NACIONALIDADE", "DESCRICAO NACIONALIDADE", "SIGLA_UF_NASCIMENTO", "CODIGO_MUNICIPIO_NASCIMENTO",
    "NOME_MUNICIPIO_NASCIMENTO", "DESPESA_MAX_CAMPANHA", "COD_SIT_TOT_TURNO", "DESC_SIT_TOT_TURNO", "NM_EMAIL"
]

full_data = pandas.read_csv("dados/consulta_cand_2016_SC.txt", sep=";", encoding="latin-1", header=None, names=columns)



code_vereador = 13
code_florianopolis = 81051
code_candidatura_deferida = 2

local_data = full_data[
    (full_data["CODIGO_CARGO"] == code_vereador) &
    (full_data["SIGLA_UE"] == code_florianopolis) &
    (full_data["COD_SITUACAO_CANDIDATURA"] == code_candidatura_deferida)
]



codes = list(range(7))
values = {
    0 : "Lê e Escreve",
    1 : "Fundamental Incompleto",
    2 : "Fundamental Completo",
    3 : "Médio Incompleto",
    4 : "Médio Completo",
    5 : "Superior Incompleto",
    6 : "Superior Completo",
}

local_data.groupby("COD_GRAU_INSTRUCAO").size().plot(kind="bar")
plt.xticks(codes, [values[i] for i in codes], rotation=60)
plt.title("Grau instrução candidatos (total={})".format(len(local_data)))
plt.show()

# for i in range(2, 9):
#     if i < 8:
#         low_instruction = local_data[local_data["COD_GRAU_INSTRUCAO"] <= i]
#     else:
#         low_instruction = local_data[local_data["COD_GRAU_INSTRUCAO"] == i]

#     low_instruction.groupby("SIGLA_PARTIDO", as_index=False).size().plot(kind='bar')
#     plt.title("Nível de instrução: {}".format(i))
#     plt.show()
