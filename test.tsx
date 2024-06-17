import { ActionFunction, redirect } from "@vercel/remix";
import db from "~/db.server";
import { apiInitiateAssistant } from "~/lib/assistant/assistantFetchers";
import { denyIfFalse, hasAccessToOrganization } from "~/utils/auth/access";
import { withUser } from "~/utils/auth/authGuard";


export const action: ActionFunction = withUser(async ({ request, user }) => {
  const formData = await request.formData();
}
