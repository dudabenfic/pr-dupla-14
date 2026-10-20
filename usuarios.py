from email_validator import validate_email, EmailNotValidError

def validar_email(email:str):
    """Validação inicial simplificada (intencionalmente incompleta)."""
    try:
        validar = validate_email(email, check_deliverability=False)
        return True, validar.normalized
    except EmailNotValidError as error:
        return False, str(error)
    

# TODO: Implementar validação de email mais robusta, incluindo verificação de domínio e formato adequado.