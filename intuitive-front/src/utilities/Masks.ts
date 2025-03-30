export const Masks = {
  CNPJ: (value: string) =>
    value.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/g, '$1.$2.$3/$4-$5'),
  CPF: (value: string) =>
    value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/g, '$1.$2.$3-$4'),
  CEP: (value: string) => value.replace(/(\d{5})(\d{3})/g, '$1-$2'),
  TELEFONE: (value: string) =>
    value.replace(/(\d{2})(\d{4})(\d{4})/g, '($1) $2-$3'),
  TELEFONEV2: (value: string) =>
    value.replace(/(\d{4})(\d{4})/g, '$1-$2'),
  CELULAR: (value: string) =>
    value.replace(/(\d{2})(\d{1})(\d{4})(\d{4})/g, '($1) $2 $3-$4'),
};
