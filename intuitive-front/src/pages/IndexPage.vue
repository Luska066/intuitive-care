<template>
  <q-page class="q-pa-lg">
    <div class="text-h3 q-mb-none text-bold q-mb-sm flex items-center">
      Contabilidade
      <q-icon name="calculate" color="purple-5" class="q-ml-md"></q-icon>
    </div>
    <q-breadcrumbs class="q-mb-lg">
      <q-breadcrumbs-el label="Inicio" class="text-h6" icon="home"/>
      <q-breadcrumbs-el label="Contabilidade" class="text-h6" icon="calculate"/>
    </q-breadcrumbs>
    <q-btn
      class="q-mb-md"
      icon="tune"
      label="Filtros"
      color="purple-9"
    >
      <q-tooltip>
        Filtros
      </q-tooltip>
      <q-menu class="q-py-md q-px-sm">
        <q-input
          v-model="filter.Registro_ANS"
          label="Registro ANS"
          class="col-12 col-sm-12 col-lg q-mb-md"
          outlined
        >
          <template v-slot:label>
            <div>
              <q-icon name="wallet"/>
              Registro ANS
            </div>
          </template>
        </q-input>
        <q-input
          v-model="filter.CNPJ"
          outlined
          label="CNPJ"
          class="q-mb-md"
          mask="##.###.###/####-##"
        >
          <template v-slot:label>
            <div>
              <q-icon name="domain"/>
              CNPJ
            </div>
          </template>
        </q-input>
         <q-input
          v-model="filter.Nome_Fantasia"
          outlined
          class="q-mb-md"
          label="Nome Fantasia"
        >
          <template v-slot:label>
            <div>
              <q-icon name="domain"/>
              Nome Fantaisa
            </div>
          </template>
        </q-input>
        <q-input
          v-model="filter.Data_Registro_ANS"
          outlined
          class="col-12 col-sm-12 col-lg q-mb-md"
          label="Data Registro ANS"
          mask="##/##/####"
        >
          <template v-slot:label>
            <div>
              <q-icon name="calendar_month"/>
              Data Registro ANS
            </div>
          </template>
        </q-input>
      </q-menu>
    </q-btn>
    <q-btn
      class="q-mb-md q-ml-md"
      icon="clear"
      label="Limpar Filtros"
      color="secondary"
    >
      <q-tooltip>
        Filtros
      </q-tooltip>
    </q-btn>
    <q-table
      flat bordered
      title="Contabilidade"
      :rows="rowsFiltered"
      style="width: 100%"
      :columns="columns"
      row-key="index"
      virtual-scroll
      v-model:pagination="pagination"
    >
      <template v-slot:body-cell-acao="props">
        <q-td>
          <q-btn
            color="purple-5"
            rounded
            @click="visualizarOperadora(props.row)"
          >
            <div>
              <q-icon name="visibility"/>
              Visualizar
            </div>
            <q-tooltip style="font-size: 15px">
              Visualizar
            </q-tooltip>
          </q-btn>
        </q-td>
      </template>
    </q-table>
    <q-dialog v-model="visibility">
      <q-card style="width: 100%; max-width: 1000px">
        <q-card-section>
          <header class="row justify-between items-center q-px-md q-py-sm q-mb-sm ">
            <div class="text-h4 text-bold ">
              Visualizar Operadora
            </div>
            <q-btn
              outline
              rounded
              @click="this.visibility = !this.visibility"
              padding="sm"
              label="fechar"
              color="blue-10"
              icon="clear"
            />
          </header>
          <q-separator/>
          <div class="row q-gutter-md q-mt-sm q-mb-md">
            <q-input
              v-model="selectedRow.Registro_ANS"
              label="Registro ANS"
              class="col-12 col-sm-12 col-lg"
              outlined
              readonly
            >
              <template v-slot:label>
                <div>
                  <q-icon name="wallet"/>
                  Registro ANS
                </div>
              </template>
            </q-input>
            <q-input
              v-model="selectedRow.Data_Registro_ANS"
              outlined
              class="col-12 col-sm-12 col-lg"
              label="Data Registro ANS"
            >
              <template v-slot:label>
                <div>
                  <q-icon name="calendar_month"/>
                  Data Registro ANS
                </div>
              </template>
            </q-input>
          </div>
          <q-input
            v-model="selectedRow.CNPJ"
            outlined
            label="CNPJ"
            readonly
            class="q-mb-md"
          >
            <template v-slot:label>
              <div>
                <q-icon name="domain"/>
                CNPJ
              </div>
            </template>
          </q-input>
          <q-input
            v-model="selectedRow.Nome_Fantasia"
            outlined
            label="Nome Fantasia"
            readonly
            class="q-mb-md"
          >
            <template v-slot:label>
              <div>
                <q-icon name="domain"/>
                Nome Fantasia
              </div>
            </template>
          </q-input>
          <q-input
            v-model="selectedRow.Razao_Social"
            outlined
            class="q-mb-md"
            readonly
            label="Razão Social"
          >
            <template v-slot:label>
              <div>
                <q-icon name="domain"/>
                Razão Social
              </div>
            </template>
          </q-input>
          <q-input
            v-model="selectedRow.Endereco_eletronico"
            outlined
            class="q-mb-md"
            readonly
            label="Endereço Eletrônico"
          >
            <template v-slot:label>
              <div>
                <q-icon name="mail"/>
                Endereço Eletrônico
              </div>
            </template>
          </q-input>
          <q-input
            v-model="selectedRow.Modalidade"
            outlined
            class="q-mb-md"
            readonly
            label="Modalidade"
          >
            <template v-slot:label>
              <div>
                <q-icon name="settings"/>
                Modalidade
              </div>
            </template>
          </q-input>
          <div class="text-bold text-h5 q-mb-md">
            Representante:
          </div>
          <q-input
            v-model="selectedRow.Representante"
            outlined
            class="q-mb-md"
            readonly
            label="Representante"
          >
            <template v-slot:label>
              <div>
                <q-icon name="person"/>
                Representante
              </div>
            </template>
          </q-input>
          <q-input
            v-model="selectedRow.Cargo_Representante"
            outlined
            class="q-mb-md"
            readonly
            label="Cargo Representante"
          >
            <template v-slot:label>
              <div>
                <q-icon name="work"/>
                Cargo Representante
              </div>
            </template>
          </q-input>
          <div class="text-bold text-h5 q-mb-md">
            Dados de Contato:
          </div>
          <div class="row">
            <q-input
              v-model="selectedRow.DDD"
              outlined
              label="DDD"
              class="col-12 col-md-2 q-mb-md"
              readonly
              mask="###"
            >
              <template v-slot:label>
                <div>
                  <q-icon name="contacts"/>
                  DDD
                </div>
              </template>
            </q-input>
            <q-input
              v-model="selectedRow.Telefone"
              outlined
              label="Telefone"
              readonly
              class="col-12 col-md q-mb-md"
            >
              <template v-slot:label>
                <div>
                  <q-icon name="phone"/>
                  Telefone
                </div>
              </template>
            </q-input>
          </div>
          <q-input
            v-model="selectedRow.Fax"
            outlined
            label="Fax"
            readonly
            class="q-mb-md"
          >
            <template v-slot:label>
              <div>
                <q-icon name="fax"/>
                Fax
              </div>
            </template>
          </q-input>
          <div class="text-bold text-h5 q-mb-md">
            Dados de Endereço:
          </div>
          <q-input
            v-model="selectedRow.CEP"
            outlined
            label="CEP"
            mask="#####-###"
            readonly
            class="q-mb-md"
          >
            <template v-slot:label>
              <div>
                <q-icon name="public"/>
                CEP
              </div>
            </template>
          </q-input>

          <q-input
            v-model="selectedRow.Regiao_de_Comercializacao"
            outlined
            class="q-mb-md"
            readonly
            label="Região de Comercialização"
          >
            <template v-slot:label>
              <div>
                <q-icon name="south_america"/>
                Região de Comercialização
              </div>
            </template>
          </q-input>
          <q-input
            outlined
            v-model="selectedRow.UF"
            class="q-mb-md"
            readonly
            label="UF"
          >
            <template v-slot:label>
              <div>
                <q-icon name="location_on"/>
                UF ( Estado )
              </div>
            </template>
          </q-input>
          <q-input
            v-model="selectedRow.Cidade"
            outlined
            class="q-mb-md"
            readonly
            label="Cidade"
          >
            <template v-slot:label>
              <div>
                <q-icon name="location_on"/>
                Cidade
              </div>
            </template>
          </q-input>
          <q-input
            v-model="selectedRow.Bairro"
            outlined
            class="q-mb-md"
            readonly
            label="Bairro"
          >
            <template v-slot:label>
              <div>
                <q-icon name="location_on"/>
                Bairro
              </div>
            </template>
          </q-input>
          <q-input
            v-model="selectedRow.Logradouro"
            outlined
            class="q-mb-md"
            readonly
            label="Logradouro"
          >
            <template v-slot:label>
              <div>
                <q-icon name="location_on"/>
                Logradouro
              </div>
            </template>
          </q-input>

          <q-input
            v-model="selectedRow.Numero"
            class="q-mb-md"
            outlined
            readonly
            label="Número"
          >
            <template v-slot:label>
              <div>
                <q-icon name="location_on"/>
                Número
              </div>
            </template>
          </q-input>

          <q-input
            v-model="selectedRow.Complemento"
            outlined
            readonly
            class="q-mb-md"
            label="Complemento"
          >
            <template v-slot:label>
              <div>
                <q-icon name="location_on"/>
                Complemento
              </div>
            </template>
          </q-input>
        </q-card-section>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import {defineComponent, ref} from 'vue';
import {api} from '../boot/axios.js'
import moment from "moment";
import {Masks} from "src/utilities/Masks.js";

export default defineComponent({
  name: 'IndexPage',
  async mounted() {
    const {data} = await api.get('/contabilidade')
    this.rows = data
  },
  computed: {
    rowsFiltered() {
      let rows = this.rows
      if(this.filter.Registro_ANS){
        rows = rows.filter((row) => row.Registro_ANS === this.filter.Registro_ANS.trim() )
      }
      if(this.filter.CNPJ){
        rows = rows.filter((row) => row.CNPJ === this.filter.CNPJ.replace(/\D/g,'').trim())
      }
      if(this.filter.Data_Registro_ANS){
        rows = rows.filter((row) => moment(row.Data_Registro_ANS).format('DD/MM/YYYY') === this.filter.Data_Registro_ANS.trim() )
      }
      if(this.filter.Nome_Fantasia){
        rows = rows.filter((row) => row.Nome_Fantasia === this.filter.Nome_Fantasia.trim() )
      }
      return rows
    }
  },
  data() {
    return {
      visibility: false,
      filter: {
        Registro_ANS: '',
        CNPJ:'',
        Data_Registro_ANS: '',
        Nome_Fantasia:''
      },
      selectedRow: {
        "Nome_Fantasia": "",
        "CEP": "",
        "Regiao_de_Comercializacao": "",
        "Modalidade": "",
        "DDD": "",
        "Data_Registro_ANS": "",
        "Logradouro": "",
        "Telefone": "",
        "Numero": "",
        "Fax": null,
        "Registro_ANS": "",
        "Complemento": null,
        "Endereco_eletronico": "",
        "Bairro": "",
        "Representante": "",
        "CNPJ": "",
        "Cidade": "",
        "Cargo_Representante": "",
        "Razao_Social": "",
        "UF": ""
      },
      rows: [],
      columns: [
        {name: 'Registro ANS', label: 'Registro ANS', field: 'Registro_ANS', sortable: true, align: 'left'},
        {
          name: 'Data Registro ANS',
          label: 'Data_Registro_ANS',
          field: (row) => moment(row.Data_Registro_ANS).format('DD/MM/YYYY'),
          sortable: true,
          align: 'left'
        },
        {name: 'CNPJ', label: 'CNPJ', field: (row) => Masks.CNPJ(row.CNPJ), sortable: true, align: 'left'},
        {name: 'Razao_Social', label: 'Razão Social', field: 'Razao_Social', align: 'left'},
        {name: 'Nome_Fantasia', label: 'Nome_Fantasia', field: (row) => row.Nome_Fantasia ?? 'Nulo', align: 'left'},
        {name: 'acao', label: 'Ações', field: (row) => row, align: 'left'}
      ],
    }
  },
  setup() {
    return {
      pagination: ref({
        rowsPerPage: 10
      })
    }
  },
  methods: {
    visualizarOperadora(row) {
      this.visibility = !this.visibility
      console.log(row);
      this.selectedRow = {
        ...row,
        Data_Registro_ANS: moment(row.Data_Registro_ANS).format('DD/MM/YYYY'),
        CNPJ: Masks.CNPJ(row.CNPJ),
        Telefone: row.Telefone != null ? Masks.TELEFONEV2(row.Telefone) : ''
      }
    }
  }
});
</script>
