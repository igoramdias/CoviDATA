import pandas as pd

def preprocess(): ##Ajeitar o csv para se adequar ao que queremos
    file = ('HIST_PAINEL_COVIDBR_06ago2020.xlsx')
    df = pd.read_excel(file)
    df = pd.DataFrame(df)

    for index, row in df.iterrows():
        if (pd.isnull(df.at[index, 'estado'])):
            df.at[index, 'estado'] = 'BR'

    index_lim = df[['codmun']].first_valid_index()
    df = df.iloc[0:index_lim,]

    df = df.drop(['regiao','municipio', 'emAcompanhamentoNovos','coduf','codmun', 'codRegiaoSaude', 'nomeRegiaoSaude', 'interior/metropolitana'], axis=1)

    df = df.rename(columns={"estado": "sigla"})
    df["estado"] = ""

    cols = df.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df = df[cols]

    df['MMNCasos'] = ""
    df['MMNObitos'] = ""
    for index, row in df.iterrows():
        if df.at[index, 'sigla'] == 'BR':
            df.at[index, 'estado'] = 'Brasil'
            if index > 13+df.sigla.ne('BR').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'RO':
            df.at[index, 'estado'] = 'Rondônia'
            if index > 13+df.sigla.ne('RO').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'AC':
            df.at[index, 'estado'] = 'Acre'
            if index > 13+df.sigla.ne('AC').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'AM':
            df.at[index, 'estado'] = 'Amazonas'
            if index > 13+df.sigla.ne('AM').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'RR':
            df.at[index, 'estado'] = 'Roraima'
            if index > 13+df.sigla.ne('RR').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'PA':
            df.at[index, 'estado'] = 'Pará'
            if index > 13+df.sigla.ne('PA').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'AP':
            df.at[index, 'estado'] = 'Amapá'
            if index > 13+df.sigla.ne('AP').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'TO':
            df.at[index, 'estado'] = 'Tocantins'
            if index > 13+df.sigla.ne('TO').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'MA':
            df.at[index, 'estado'] = 'Maranhão'
            if index > 13+df.sigla.ne('MA').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'PI':
            df.at[index, 'estado'] = 'Piauí'
            if index > 13+df.sigla.ne('PI').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'CE':
            df.at[index, 'estado'] = 'Ceará'
            if index > 13+df.sigla.ne('CE').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'RN':
            df.at[index, 'estado'] = 'Rio Grande do Norte'
            if index > 13+df.sigla.ne('RN').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'PB':
            df.at[index, 'estado'] = 'Paraíba'
            if index > 13+df.sigla.ne('PB').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'PE':
            df.at[index, 'estado'] = 'Pernambuco'
            if index > 13+df.sigla.ne('PE').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'AL':
            df.at[index, 'estado'] = 'Alagoas'
            if index > 13+df.sigla.ne('AL').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'SE':
            df.at[index, 'estado'] = 'Sergipe'
            if index > 13+df.sigla.ne('SE').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'BA':
            df.at[index, 'estado'] = 'Bahia'
            if index > 13+df.sigla.ne('BA').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'MG':
            df.at[index, 'estado'] = 'Minas Gerais'
            if index > 13+df.sigla.ne('MG').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'ES':
            df.at[index, 'estado'] = 'Espírito Santo'
            if index > 13+df.sigla.ne('ES').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'RJ':
            df.at[index, 'estado'] = 'Rio de Janeiro'
            if index > 13+df.sigla.ne('RJ').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'SP':
            df.at[index, 'estado'] = 'São Paulo'
            if index > 13+df.sigla.ne('SP').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'PR':
            df.at[index, 'estado'] = 'Paraná'
            if index > 13+df.sigla.ne('PR').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'SC':
            df.at[index, 'estado'] = 'Santa Catarina'
            if index > 13+df.sigla.ne('SC').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'RS':
            df.at[index, 'estado'] = 'Rio Grande do Sul'
            if index > 13+df.sigla.ne('RS').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'MS':
            df.at[index, 'estado'] = 'Mato Grosso do Sul'
            if index > 13+df.sigla.ne('MS').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'MT':
            df.at[index, 'estado'] = 'Mato Grosso'
            if index > 13+df.sigla.ne('MT').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'GO':
            df.at[index, 'estado'] = 'Goiás'
            if index > 13+df.sigla.ne('GO').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]
        elif df.at[index, 'sigla'] == 'DF':
            df.at[index, 'estado'] = 'Distrito Federal'     
            if index > 13+df.sigla.ne('DF').idxmin():
                df.at[index, 'MMNCasos'] = df[['casosNovos']].iloc[index-14:index].mean().values[0]
                df.at[index, 'MMNObitos'] = df[['obitosNovos']].iloc[index-14:index].mean().values[0]   

    df.to_csv(r'covid_data.csv', index = False)

preprocess()