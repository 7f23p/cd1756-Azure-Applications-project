# Write-up

> ### Analyze, choose, and justify the appropriate resource option for deploying the app.
>
> *For **both** a VM or App Service solution for the CMS app:*
> - *Analyze costs, scalability, availability, and workflow*
> - *Choose the appropriate solution (VM or App Service) for deploying the app*
> - *Justify your choice*

I chose App Service over VM: Primarily for simplicity, as I don't have to manage the underlying operating system and it comes with reasonable security default settings. Additionally, App Services appears to be lower cost than VMs, specially when factoring-in ongoing maintenance costs.

Although both options could have theoretically comparable availability, it comes at a much higher cost for VMs, as OS maintance, updates, reboots, etc. might require careful planning. Therefore high-availability in App Services is handlead seamlessly. To be more specific, the web app service appears to match the capabilities of a VM. However, considering the additional user configurations and potential risks associated with a VM, the web app likely surpasses in terms of reliability and uptime. The need for regular restarts and operating system maintenance on a VM could potentially disrupt service availability, a concern largely mitigated by the web app service.

Scalability with the web app service is another aspect that suits my project's needs well. Given the current scale of my application, the ability to upscale in the future with minimal cost and effort is a significant advantage over a VM, where scaling can involve more complex configurations and higher expenses.

Therefore I choose App Service over VM after considering simplicity, availability and cost aspect.
### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

The app would need to include with boilerplate to automate deployments in the VM. The VM itself should already contain all 
I would consider a Virtual Machine in the following cases:

- Increased Complexity and Customization Needs: If the application evolves to require highly specific custom configurations that are not supported by a Web App Service.
- If the CMS had stricter security requirements where App Service defaults are insufficient (e.g. custom OS tweaks).
- When launching complex projects with several non-standard interdependent compontents.

In summary, I would consider a shift towards a VM if my application undergoes changes that demand higher customization, enhanced security, specific performance requirements (load balancing and traffic management, etc.), or integration with particular technologies or systems. These changes would warrant the need for the more controlled, flexible, and potentially resource-intensive environment that a VM can offer.
