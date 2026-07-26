import boto3
import sys
import time

REGION = "us-east-1"
STACK_NAME = "Stack-Automated-EC2-SDK"
TEMPLATE_PATH = "desafioCloudFormation/infraestrutura.yaml"

cf_client = boto3.client("cloudformation", region_name=REGION)


def load_template(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def create_stack():
    print(f"[SDK] Iniciando criacao da stack: {STACK_NAME}...")
    template_body = load_template(TEMPLATE_PATH)

    response = cf_client.create_stack(
        StackName=STACK_NAME,
        TemplateBody=template_body,
    )
    print(f"Stack enviada com sucesso! Stack ID: {response['StackId']}")

    print("Aguardando conclusao do provisionamento no CloudFormation (Waiter)...")
    waiter = cf_client.get_waiter("stack_create_complete")
    waiter.wait(StackName=STACK_NAME)
    print("Stack e recursos criados com sucesso!")


def get_stack_outputs():
    response = cf_client.describe_stacks(StackName=STACK_NAME)
    outputs = response["Stacks"][0].get("Outputs", [])

    print("\n--- OUTPUTS DA INFRAESTRUTURA PROVISIONADA ---")
    for output in outputs:
        print(f"• {output['OutputKey']}: {output['OutputValue']}")


def delete_stack():
    print(f"\n[FinOps] Iniciando delecao automatica da stack {STACK_NAME}...")
    cf_client.delete_stack(StackName=STACK_NAME)

    waiter = cf_client.get_waiter("stack_delete_complete")
    waiter.wait(StackName=STACK_NAME)
    print("Stack e recursos deletados com sucesso para evitar custos!")


if __name__ == "__main__":
    try:
        # 1. Provisiona a infraestrutura
        create_stack()
        
        # 2. Exibe os dados gerados (IP / URL)
        get_stack_outputs()
        
        # Pausa de 15 segundos apenas para permitir visualizacao no log do pipeline
        print("\nAguardando 2 minutos antes da limpeza de seguranca...")
        time.sleep(120)
        
        # 3. Limpeza FinOps
        delete_stack()

    except Exception as e:
        print(f"Erro na execucao da automacao: {e}", file=sys.stderr)
        sys.exit(1)